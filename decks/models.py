from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def current_year():
    return timezone.now().year


def current_month():
    return timezone.now().month


class FirstPage(models.Model):
    MONTH_CHOICES = [
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
    ]

    image = models.ImageField(upload_to="first_pages/")
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.PositiveIntegerField(default=current_year)
    month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES, default=current_month)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "first page"
        verbose_name_plural = "first pages"

    def __str__(self):
        return self.title


class NextPage(models.Model):
    title = models.CharField(max_length=200, default="Key Metrics & Outcomes")
    description = models.CharField(max_length=200, default="Coding - Overall")
    score_title = models.CharField(max_length=100, default="Quality Score")
    score_value = models.CharField(max_length=30, default="97.4%")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "next page"
        verbose_name_plural = "next pages"

    def __str__(self):
        return self.title


class NextPageCard(models.Model):
    page = models.ForeignKey(NextPage, related_name="cards", on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=30)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "next page card"
        verbose_name_plural = "next page cards"

    def clean(self):
        if self.page_id and self.page.cards.exclude(pk=self.pk).count() >= 10:
            raise ValidationError("Only 10 cards are allowed for one next page.")

    def __str__(self):
        return f"{self.label}: {self.value}"


class AgencyPage(models.Model):
    title = models.CharField(max_length=200, default="Client Additions")
    content = models.TextField(default="New clients, strong partnerships, and a pipeline that keeps moving forward.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "agency page"
        verbose_name_plural = "agency pages"

    def __str__(self):
        return self.title


class AgencyName(models.Model):
    page = models.ForeignKey(AgencyPage, related_name="agencies", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "agency name"
        verbose_name_plural = "agency names"

    def __str__(self):
        return self.name


class BulletPage(models.Model):
    title = models.CharField(max_length=200, default="Key Metrics & Outcomes")
    description = models.CharField(max_length=200, default="RCM")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "bullet page"
        verbose_name_plural = "bullet pages"

    def __str__(self):
        return self.title


class BulletCard(models.Model):
    page = models.ForeignKey(BulletPage, related_name="cards", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "bullet card"
        verbose_name_plural = "bullet cards"

    def __str__(self):
        return self.title


class BulletItem(models.Model):
    card = models.ForeignKey(BulletCard, related_name="items", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "bullet item"
        verbose_name_plural = "bullet items"

    def __str__(self):
        return self.text


class ClientDatePage(models.Model):
    title = models.CharField(max_length=200, default="Client Additions")
    content = models.TextField(default="New clients, strong partnerships, and a pipeline that keeps moving forward.")
    description = models.CharField(max_length=200, default="RCM")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "client date page"
        verbose_name_plural = "client date pages"

    def __str__(self):
        return self.title


class ClientDateItem(models.Model):
    page = models.ForeignKey(ClientDatePage, related_name="clients", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    went_live_on = models.DateField()
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "client date item"
        verbose_name_plural = "client date items"

    def __str__(self):
        return self.name


class ClientSaysPage(models.Model):
    heading = models.CharField(max_length=200, default="What Our Clients Say...")
    client_description = models.TextField()
    client_name = models.CharField(max_length=200, help_text="Client or agency name shown under the quote.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "client says page"
        verbose_name_plural = "client says pages"

    def __str__(self):
        return self.heading


class ClientSaysPerson(models.Model):
    page = models.ForeignKey(ClientSaysPage, related_name="people", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="client_says/")
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "client says person"
        verbose_name_plural = "client says people"

    @property
    def is_team_leader(self):
        return "teamleader" in self.designation.lower().replace(" ", "")

    def __str__(self):
        return self.name


class GalleryPage(models.Model):
    caption = models.CharField(max_length=200, default="Tongue Twister Challenge")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "gallery page"
        verbose_name_plural = "gallery pages"

    def __str__(self):
        return self.caption


class GalleryImage(models.Model):
    page = models.ForeignKey(GalleryPage, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="gallery/")
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "gallery image"
        verbose_name_plural = "gallery images"

    def clean(self):
        if self.page_id and self.page.images.exclude(pk=self.pk).count() >= 5:
            raise ValidationError("Only 5 images are allowed for one gallery page.")

    def __str__(self):
        return f"{self.page.caption} image {self.order}"


class CaptionSlidePage(models.Model):
    caption = models.CharField(max_length=200, default="Best wishes for the year ahead!")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "caption slide page"
        verbose_name_plural = "caption slide pages"

    def __str__(self):
        return self.caption


class CaptionSlideImage(models.Model):
    page = models.ForeignKey(CaptionSlidePage, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="caption_slides/")
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "caption slide image"
        verbose_name_plural = "caption slide images"

    def clean(self):
        if self.page_id and self.page.images.exclude(pk=self.pk).count() >= 3:
            raise ValidationError("Only 3 images are allowed for one caption slide page.")

    def __str__(self):
        return f"{self.page.caption} image {self.order}"


class NewJoinersPage(models.Model):
    title = models.CharField(max_length=200, default="New Joiners")
    caption = models.CharField(max_length=200, default="Welcome aboard! Glad to have you with us!")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "new joiners page"
        verbose_name_plural = "new joiners pages"

    def __str__(self):
        return self.title


class NewJoiner(models.Model):
    page = models.ForeignKey(NewJoinersPage, related_name="joiners", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="new_joiners/")
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "new joiner"
        verbose_name_plural = "new joiners"

    def clean(self):
        if self.page_id and self.page.joiners.exclude(pk=self.pk).count() >= 10:
            raise ValidationError("Only 10 joiners are allowed for one new joiners page.")

    def __str__(self):
        return self.name


class PromotionsPage(models.Model):
    title = models.CharField(max_length=200, default="Promotions")
    caption = models.CharField(max_length=200, default="Rising to new heights")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "promotions page"
        verbose_name_plural = "promotions pages"

    def __str__(self):
        return self.title


class Promotion(models.Model):
    page = models.ForeignKey(PromotionsPage, related_name="promotions", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="promotions/")
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "promotion"
        verbose_name_plural = "promotions"

    def clean(self):
        if self.page_id and self.page.promotions.exclude(pk=self.pk).count() >= 10:
            raise ValidationError("Only 10 promotions are allowed for one promotions page.")

    def __str__(self):
        return self.name


class KudosMomentPage(models.Model):
    CARDS_ONLY = "cards_only"
    IMAGE_WITH_CARDS = "image_with_cards"
    DISPLAY_CHOICES = [
        (CARDS_ONLY, "Cards only"),
        (IMAGE_WITH_CARDS, "Image with cards"),
    ]

    title = models.CharField(max_length=200, default="Kudos Moments")
    display_type = models.CharField(max_length=30, choices=DISPLAY_CHOICES, default=IMAGE_WITH_CARDS)
    image = models.ImageField(upload_to="kudos_moments/", blank=True)
    name = models.CharField(max_length=200, blank=True, default="")
    designation = models.CharField(max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "kudos moment page"
        verbose_name_plural = "kudos moment pages"

    def __str__(self):
        return self.title


class KudosMomentCard(models.Model):
    page = models.ForeignKey(KudosMomentPage, related_name="cards", on_delete=models.CASCADE)
    value = models.CharField(max_length=30)
    label = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "kudos moment card"
        verbose_name_plural = "kudos moment cards"

    def clean(self):
        if self.page_id and self.page.cards.exclude(pk=self.pk).count() >= 10:
            raise ValidationError("Only 10 cards are allowed for one kudos moment page.")

    def __str__(self):
        return f"{self.value} {self.label}"


class SpecialAppreciationPage(models.Model):
    title = models.CharField(max_length=200, default="Special Appreciation")
    image = models.ImageField(upload_to="special_appreciations/")
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "special appreciation page"
        verbose_name_plural = "special appreciation pages"

    def __str__(self):
        return self.title


class KudosBulletMomentPage(models.Model):
    CARDS_ONLY = "cards_only"
    IMAGE_WITH_CARDS = "image_with_cards"
    DISPLAY_CHOICES = [
        (CARDS_ONLY, "Cards only"),
        (IMAGE_WITH_CARDS, "Image with cards"),
    ]

    title = models.CharField(max_length=200, default="Kudos Moments")
    display_type = models.CharField(max_length=30, choices=DISPLAY_CHOICES, default=IMAGE_WITH_CARDS)
    image = models.ImageField(upload_to="kudos_bullet_moments/", blank=True)
    name = models.CharField(max_length=200, blank=True, default="")
    designation = models.CharField(max_length=200, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "kudos bullet moment page"
        verbose_name_plural = "kudos bullet moment pages"

    def __str__(self):
        return self.title


class KudosBulletMomentCard(models.Model):
    METRIC = "metric"
    TEXT = "text"
    BULLETS = "bullets"
    CARD_TYPE_CHOICES = [
        (METRIC, "Metric"),
        (TEXT, "Text"),
        (BULLETS, "Bullets"),
    ]

    page = models.ForeignKey(KudosBulletMomentPage, related_name="cards", on_delete=models.CASCADE)
    card_type = models.CharField(max_length=20, choices=CARD_TYPE_CHOICES, default=METRIC)
    value = models.CharField(max_length=60, blank=True, default="")
    label = models.CharField(max_length=200, blank=True, default="")
    title = models.CharField(max_length=200, blank=True, default="")
    content = models.TextField(blank=True, default="", help_text="For bullets, enter one item per line.")
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order"]
        verbose_name = "kudos bullet moment card"
        verbose_name_plural = "kudos bullet moment cards"

    def clean(self):
        if self.page_id and self.page.cards.exclude(pk=self.pk).count() >= 10:
            raise ValidationError("Only 10 cards are allowed for one kudos bullet moment page.")

    @property
    def bullet_items(self):
        return [line.strip() for line in self.content.splitlines() if line.strip()]

    def __str__(self):
        return self.title or self.label or self.value or f"Card {self.order}"
