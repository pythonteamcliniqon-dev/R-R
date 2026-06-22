from django.contrib import admin

from .models import (
    AgencyName,
    AgencyPage,
    BulletCard,
    BulletItem,
    BulletPage,
    CareerOpportunityJob,
    CareerOpportunityPage,
    CaptionSlideImage,
    CaptionSlidePage,
    ClientDateItem,
    ClientDatePage,
    ClientSaysPage,
    ClientSaysPerson,
    FirstPage,
    GalleryImage,
    GalleryPage,
    KudosBulletMomentCard,
    KudosBulletMomentPage,
    KudosMomentCard,
    KudosMomentPage,
    NewJoiner,
    NewJoinersPage,
    NextPage,
    NextPageCard,
    Promotion,
    PromotionsPage,
    SpecialAppreciationPage,
)


@admin.register(FirstPage)
class FirstPageAdmin(admin.ModelAdmin):
    list_display = ("title", "month", "year", "created_at")
    list_filter = ("year", "month")
    search_fields = ("title", "description")


class NextPageCardInline(admin.TabularInline):
    model = NextPageCard
    extra = 5
    max_num = 10


@admin.register(NextPage)
class NextPageAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "score_title", "score_value", "created_at")
    search_fields = ("title", "description", "score_title", "score_value")
    inlines = [NextPageCardInline]


class AgencyNameInline(admin.TabularInline):
    model = AgencyName
    extra = 1


@admin.register(AgencyPage)
class AgencyPageAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
    inlines = [AgencyNameInline]


class BulletItemInline(admin.TabularInline):
    model = BulletItem
    extra = 1


@admin.register(BulletCard)
class BulletCardAdmin(admin.ModelAdmin):
    list_display = ("title", "page", "order")
    inlines = [BulletItemInline]


class BulletCardInline(admin.TabularInline):
    model = BulletCard
    extra = 1


@admin.register(BulletPage)
class BulletPageAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at")
    search_fields = ("title", "description")
    inlines = [BulletCardInline]


class ClientDateItemInline(admin.TabularInline):
    model = ClientDateItem
    extra = 1


@admin.register(ClientDatePage)
class ClientDatePageAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at")
    search_fields = ("title", "content", "description")
    inlines = [ClientDateItemInline]


class ClientSaysPersonInline(admin.TabularInline):
    model = ClientSaysPerson
    extra = 1


@admin.register(ClientSaysPage)
class ClientSaysPageAdmin(admin.ModelAdmin):
    list_display = ("heading", "client_name", "created_at")
    search_fields = ("heading", "client_description", "client_name")
    inlines = [ClientSaysPersonInline]


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1
    max_num = 5


@admin.register(GalleryPage)
class GalleryPageAdmin(admin.ModelAdmin):
    list_display = ("caption", "created_at")
    search_fields = ("caption",)
    inlines = [GalleryImageInline]


class CaptionSlideImageInline(admin.TabularInline):
    model = CaptionSlideImage
    extra = 1
    max_num = 3


@admin.register(CaptionSlidePage)
class CaptionSlidePageAdmin(admin.ModelAdmin):
    list_display = ("caption", "created_at")
    search_fields = ("caption",)
    inlines = [CaptionSlideImageInline]


class NewJoinerInline(admin.TabularInline):
    model = NewJoiner
    extra = 1
    max_num = 10


@admin.register(NewJoinersPage)
class NewJoinersPageAdmin(admin.ModelAdmin):
    list_display = ("title", "caption", "created_at")
    search_fields = ("title", "caption")
    inlines = [NewJoinerInline]


class PromotionInline(admin.TabularInline):
    model = Promotion
    extra = 1
    max_num = 10


@admin.register(PromotionsPage)
class PromotionsPageAdmin(admin.ModelAdmin):
    list_display = ("title", "caption", "created_at")
    search_fields = ("title", "caption")
    inlines = [PromotionInline]


class KudosMomentCardInline(admin.TabularInline):
    model = KudosMomentCard
    extra = 1
    max_num = 10


@admin.register(KudosMomentPage)
class KudosMomentPageAdmin(admin.ModelAdmin):
    list_display = ("title", "display_type", "name", "designation", "created_at")
    search_fields = ("title", "name", "designation")
    inlines = [KudosMomentCardInline]


@admin.register(SpecialAppreciationPage)
class SpecialAppreciationPageAdmin(admin.ModelAdmin):
    list_display = ("title", "name", "designation", "created_at")
    search_fields = ("title", "name", "designation", "content", "author")


class KudosBulletMomentCardInline(admin.TabularInline):
    model = KudosBulletMomentCard
    extra = 1
    max_num = 10


@admin.register(KudosBulletMomentPage)
class KudosBulletMomentPageAdmin(admin.ModelAdmin):
    list_display = ("title", "display_type", "name", "designation", "created_at")
    search_fields = ("title", "name", "designation")
    inlines = [KudosBulletMomentCardInline]


class CareerOpportunityJobInline(admin.TabularInline):
    model = CareerOpportunityJob
    extra = 1
    max_num = 10


@admin.register(CareerOpportunityPage)
class CareerOpportunityPageAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
    inlines = [CareerOpportunityJobInline]
