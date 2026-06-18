from django import forms

from .models import (
    AgencyName,
    AgencyPage,
    BulletPage,
    CaptionSlidePage,
    ClientDatePage,
    ClientSaysPage,
    FirstPage,
    GalleryPage,
    KudosBulletMomentPage,
    KudosMomentPage,
    NewJoinersPage,
    NextPage,
    NextPageCard,
    PromotionsPage,
    SpecialAppreciationPage,
)


class FirstPageForm(forms.ModelForm):
    class Meta:
        model = FirstPage
        fields = ["image", "title", "description", "year", "month"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "year": forms.NumberInput(attrs={"min": 1900, "max": 2100}),
        }


class NextPageForm(forms.ModelForm):
    class Meta:
        model = NextPage
        fields = ["title", "description", "score_title", "score_value"]


class NextPageCardForm(forms.ModelForm):
    class Meta:
        model = NextPageCard
        fields = ["label", "value", "order"]
        widgets = {
            "order": forms.NumberInput(attrs={"min": 1, "max": 10}),
        }


NextPageCardFormSet = forms.inlineformset_factory(
    NextPage,
    NextPageCard,
    form=NextPageCardForm,
    extra=10,
    max_num=10,
    validate_max=True,
    can_delete=False,
)


class AgencyPageForm(forms.ModelForm):
    class Meta:
        model = AgencyPage
        fields = ["title", "content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4}),
        }


class AgencyNameForm(forms.ModelForm):
    class Meta:
        model = AgencyName
        fields = ["name", "order"]
        widgets = {
            "order": forms.NumberInput(attrs={"min": 1}),
        }


AgencyNameFormSet = forms.inlineformset_factory(
    AgencyPage,
    AgencyName,
    form=AgencyNameForm,
    extra=1,
    can_delete=True,
)


class BulletPageForm(forms.ModelForm):
    class Meta:
        model = BulletPage
        fields = ["title", "description"]


class ClientDatePageForm(forms.ModelForm):
    class Meta:
        model = ClientDatePage
        fields = ["title", "content", "description"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4}),
        }


class ClientSaysPageForm(forms.ModelForm):
    class Meta:
        model = ClientSaysPage
        fields = ["heading", "client_description", "client_name"]
        widgets = {
            "client_description": forms.Textarea(attrs={"rows": 4}),
        }


class GalleryPageForm(forms.ModelForm):
    class Meta:
        model = GalleryPage
        fields = ["caption"]


class CaptionSlidePageForm(forms.ModelForm):
    class Meta:
        model = CaptionSlidePage
        fields = ["caption"]


class NewJoinersPageForm(forms.ModelForm):
    class Meta:
        model = NewJoinersPage
        fields = ["title", "caption"]


class PromotionsPageForm(forms.ModelForm):
    class Meta:
        model = PromotionsPage
        fields = ["title", "caption"]


class KudosMomentPageForm(forms.ModelForm):
    class Meta:
        model = KudosMomentPage
        fields = ["title", "display_type", "image", "name", "designation"]


class SpecialAppreciationPageForm(forms.ModelForm):
    class Meta:
        model = SpecialAppreciationPage
        fields = ["title", "image", "name", "designation", "content", "author"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 8}),
        }


class KudosBulletMomentPageForm(forms.ModelForm):
    class Meta:
        model = KudosBulletMomentPage
        fields = ["title", "display_type", "image", "name", "designation"]
