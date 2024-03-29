from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Category, Genre, Movie, MovieShorts, Actor, Rating, RatingStar, Reviews
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""

    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = "__all__"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""

    list_display = ("name", "url")
    list_display_links = ("name",)


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""

    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class MovieShortsInline(admin.TabularInline):
    model = MovieShorts
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фильмы"""

    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MovieShortsInline, ReviewInline]
    save_on_top = True
    save_as = True
    readonly_fields = ("get_image",)
    list_editable = ("draft",)
    actions = ["published", "unpublished"]
    form = MovieAdminForm
    fieldsets = (
        ("Title & Tagline", {"fields": (("title", "tagline"),)}),
        ("Image & Description", {"fields": ("description", ("poster", "get_image"))}),
        ("Date", {"fields": (("year", "world_premiere", "country"),)}),
        ("Actors", {"classes": ("collapse",), "fields": (("actors", "directors", "genres", "category"),)}),
        ("Budget", {"fields": (("budget", "fees_in_usa", "fees_in_world"),)}),
        ("Options", {"fields": (("url", "draft"),)}),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Постер"

    def unpublished(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def published(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    published.short_description = "Опубликовать"
    published.allowed_permissions = ("change",)

    unpublished.short_description = "Снять с публикации"
    unpublished.allowed_permissions = ("change",)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""

    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""

    list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актеры"""

    list_display = ("name", "age", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""

    list_display = ("star", "movie", "ip")


@admin.register(MovieShorts)
class MovieShortsAdmin(admin.ModelAdmin):
    """Кадры из фильма"""

    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Изображение"


admin.site.register(RatingStar)

