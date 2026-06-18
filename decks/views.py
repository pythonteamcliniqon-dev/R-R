from django.shortcuts import redirect, render

from .forms import (
    AgencyNameFormSet,
    AgencyPageForm,
    BulletPageForm,
    CaptionSlidePageForm,
    ClientDatePageForm,
    ClientSaysPageForm,
    FirstPageForm,
    GalleryPageForm,
    KudosBulletMomentPageForm,
    KudosMomentPageForm,
    NewJoinersPageForm,
    NextPageCardFormSet,
    NextPageForm,
    PromotionsPageForm,
    SpecialAppreciationPageForm,
)
from .models import (
    AgencyPage,
    BulletCard,
    BulletItem,
    BulletPage,
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
    Promotion,
    PromotionsPage,
    SpecialAppreciationPage,
)


def first_page_list(request):
    first_pages = FirstPage.objects.all()
    return render(request, "decks/first_page_list.html", {"first_pages": first_pages})


def next_page_view(request):
    next_page = NextPage.objects.prefetch_related("cards").first()
    return render(request, "decks/next_page_view.html", {"next_page": next_page})


def agency_page_view(request):
    agency_page = AgencyPage.objects.prefetch_related("agencies").first()
    agencies = agency_page.agencies.all() if agency_page else []
    agency_image = "decks/img/image-7.png"
    if agency_page and "churn" in agency_page.title.lower():
        agency_image = "decks/img/image-8.png"
    return render(
        request,
        "decks/agency_page_view.html",
        {
            "agency_page": agency_page,
            "agencies": agencies,
            "agency_image": agency_image,
        },
    )


def bullet_page_view(request):
    bullet_page = BulletPage.objects.prefetch_related("cards__items").first()
    return render(request, "decks/bullet_page_view.html", {"bullet_page": bullet_page})


def client_date_page_view(request):
    client_page = ClientDatePage.objects.prefetch_related("clients").first()
    return render(request, "decks/client_date_page_view.html", {"client_page": client_page})


def client_says_page_view(request):
    says_page = ClientSaysPage.objects.prefetch_related("people").first()
    people = list(says_page.people.all()) if says_page else []
    team_leader = next((person for person in people if person.is_team_leader), None)
    regular_people = [person for person in people if person != team_leader]
    return render(
        request,
        "decks/client_says_page_view.html",
        {
            "says_page": says_page,
            "team_leader": team_leader,
            "regular_people": regular_people,
            "people_count": len(regular_people),
        },
    )


def gallery_page_view(request):
    gallery_page = GalleryPage.objects.prefetch_related("images").first()
    return render(request, "decks/gallery_page_view.html", {"gallery_page": gallery_page})


def caption_slide_page_view(request):
    caption_slide_page = CaptionSlidePage.objects.prefetch_related("images").first()
    return render(
        request,
        "decks/caption_slide_page_view.html",
        {"caption_slide_page": caption_slide_page},
    )


def new_joiners_view(request):
    new_joiners_page = NewJoinersPage.objects.prefetch_related("joiners").first()
    return render(
        request,
        "decks/new_joiners_view.html",
        {"new_joiners_page": new_joiners_page},
    )


def promotions_view(request):
    promotions_page = PromotionsPage.objects.prefetch_related("promotions").first()
    return render(
        request,
        "decks/promotions_view.html",
        {"promotions_page": promotions_page},
    )


def kudos_moments_view(request):
    kudos_page = KudosMomentPage.objects.prefetch_related("cards").first()
    return render(
        request,
        "decks/kudos_moments_view.html",
        {"kudos_page": kudos_page},
    )


def kudos_bullet_moments_view(request):
    kudos_page = KudosBulletMomentPage.objects.prefetch_related("cards").first()
    return render(
        request,
        "decks/kudos_bullet_moments_view.html",
        {"kudos_page": kudos_page},
    )


def special_appreciation_view(request):
    special_page = SpecialAppreciationPage.objects.first()
    return render(
        request,
        "decks/special_appreciation_view.html",
        {"special_page": special_page},
    )


def dashboard(request):
    if request.method == "POST":
        form = FirstPageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("first_page_list")
    else:
        form = FirstPageForm()

    first_pages = FirstPage.objects.all()
    return render(
        request,
        "decks/dashboard.html",
        {"form": form, "first_pages": first_pages, "active_menu": "first"},
    )


def next_page_dashboard(request):
    page = NextPage.objects.first()

    if request.method == "POST":
        form = NextPageForm(request.POST, instance=page)
        formset = NextPageCardFormSet(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            formset = NextPageCardFormSet(request.POST, instance=page)
            if formset.is_valid():
                formset.save()
                return redirect("next_page_dashboard")
    else:
        form = NextPageForm(instance=page)
        formset = NextPageCardFormSet(instance=page)

    next_pages = NextPage.objects.prefetch_related("cards").all()
    return render(
        request,
        "decks/next_page_dashboard.html",
        {
            "form": form,
            "formset": formset,
            "next_pages": next_pages,
            "active_menu": "next",
        },
    )


def agency_page_dashboard(request):
    page = AgencyPage.objects.first()

    if request.method == "POST":
        form = AgencyPageForm(request.POST, instance=page)
        formset = AgencyNameFormSet(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            formset = AgencyNameFormSet(request.POST, instance=page)
            if formset.is_valid():
                formset.save()
                return redirect("agency_page_dashboard")
    else:
        form = AgencyPageForm(instance=page)
        formset = AgencyNameFormSet(instance=page)

    agency_pages = AgencyPage.objects.prefetch_related("agencies").all()
    return render(
        request,
        "decks/agency_page_dashboard.html",
        {
            "form": form,
            "formset": formset,
            "agency_pages": agency_pages,
            "active_menu": "agency",
        },
    )


def bullet_page_dashboard(request):
    page = BulletPage.objects.prefetch_related("cards__items").first()

    if request.method == "POST":
        form = BulletPageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            page.cards.all().delete()

            card_titles = request.POST.getlist("card_title")
            bullet_groups = request.POST.getlist("card_bullets")
            for index, card_title in enumerate(card_titles, start=1):
                title = card_title.strip()
                if not title:
                    continue

                card = BulletCard.objects.create(page=page, title=title, order=index)
                bullets = bullet_groups[index - 1].splitlines() if index - 1 < len(bullet_groups) else []
                for bullet_index, bullet in enumerate(bullets, start=1):
                    text = bullet.strip()
                    if text:
                        BulletItem.objects.create(card=card, text=text, order=bullet_index)

            return redirect("bullet_page_dashboard")
    else:
        form = BulletPageForm(instance=page)

    bullet_pages = BulletPage.objects.prefetch_related("cards__items").all()
    return render(
        request,
        "decks/bullet_page_dashboard.html",
        {
            "form": form,
            "page": page,
            "bullet_pages": bullet_pages,
            "active_menu": "bullet",
        },
    )


def client_date_page_dashboard(request):
    page = ClientDatePage.objects.prefetch_related("clients").first()

    if request.method == "POST":
        form = ClientDatePageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            page.clients.all().delete()

            names = request.POST.getlist("client_name")
            dates = request.POST.getlist("went_live_on")
            orders = request.POST.getlist("client_order")
            for index, name in enumerate(names, start=1):
                client_name = name.strip()
                went_live_on = dates[index - 1] if index - 1 < len(dates) else ""
                order = orders[index - 1] if index - 1 < len(orders) else index
                if client_name and went_live_on:
                    ClientDateItem.objects.create(
                        page=page,
                        name=client_name,
                        went_live_on=went_live_on,
                        order=order or index,
                    )

            return redirect("client_date_page_dashboard")
    else:
        form = ClientDatePageForm(instance=page)

    client_pages = ClientDatePage.objects.prefetch_related("clients").all()
    return render(
        request,
        "decks/client_date_page_dashboard.html",
        {
            "form": form,
            "page": page,
            "client_pages": client_pages,
            "active_menu": "client_date",
        },
    )


def client_says_page_dashboard(request):
    page = ClientSaysPage.objects.prefetch_related("people").first()

    if request.method == "POST":
        form = ClientSaysPageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            existing_people = {str(person.pk): person for person in page.people.all()}
            seen_people = []

            ids = request.POST.getlist("person_id")
            names = request.POST.getlist("person_name")
            designations = request.POST.getlist("person_designation")
            orders = request.POST.getlist("person_order")
            images = request.FILES.getlist("person_image")

            for index, name in enumerate(names, start=1):
                person_name = name.strip()
                designation = designations[index - 1].strip() if index - 1 < len(designations) else ""
                order = orders[index - 1] if index - 1 < len(orders) else index
                person_id = ids[index - 1] if index - 1 < len(ids) else ""
                image = images[index - 1] if index - 1 < len(images) else None

                if not person_name or not designation:
                    continue

                person = existing_people.get(person_id) if person_id else ClientSaysPerson(page=page)
                person.name = person_name
                person.designation = designation
                person.order = order or index
                if image:
                    person.image = image
                if person.image:
                    person.save()
                    seen_people.append(person.pk)

            page.people.exclude(pk__in=seen_people).delete()
            return redirect("client_says_page_dashboard")
    else:
        form = ClientSaysPageForm(instance=page)

    says_pages = ClientSaysPage.objects.prefetch_related("people").all()
    return render(
        request,
        "decks/client_says_page_dashboard.html",
        {
            "form": form,
            "page": page,
            "says_pages": says_pages,
            "active_menu": "client_says",
        },
    )


def gallery_page_dashboard(request):
    page = GalleryPage.objects.prefetch_related("images").first()

    if request.method == "POST":
        form = GalleryPageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            existing_images = {str(image.pk): image for image in page.images.all()}
            seen_images = []

            ids = request.POST.getlist("gallery_image_id")
            orders = request.POST.getlist("gallery_image_order")

            for index in range(5):
                image_id = ids[index] if index < len(ids) else ""
                order = orders[index] if index < len(orders) else index + 1
                upload = request.FILES.get(f"gallery_image_{index + 1}")

                gallery_image = existing_images.get(image_id) if image_id else GalleryImage(page=page)
                gallery_image.order = order or index + 1
                if upload:
                    gallery_image.image = upload
                if gallery_image.image:
                    gallery_image.save()
                    seen_images.append(gallery_image.pk)

            page.images.exclude(pk__in=seen_images).delete()
            return redirect("gallery_page_dashboard")
    else:
        form = GalleryPageForm(instance=page)

    gallery_pages = GalleryPage.objects.prefetch_related("images").all()
    existing_images = list(page.images.all()) if page else []
    gallery_image_rows = existing_images + [None] * (5 - len(existing_images))
    return render(
        request,
        "decks/gallery_page_dashboard.html",
        {
            "form": form,
            "page": page,
            "gallery_image_rows": gallery_image_rows,
            "gallery_pages": gallery_pages,
            "active_menu": "gallery",
        },
    )


def caption_slide_page_dashboard(request):
    page = CaptionSlidePage.objects.prefetch_related("images").first()

    if request.method == "POST":
        form = CaptionSlidePageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            existing_images = {str(image.pk): image for image in page.images.all()}
            seen_images = []

            ids = request.POST.getlist("caption_slide_image_id")
            orders = request.POST.getlist("caption_slide_image_order")

            for index in range(3):
                image_id = ids[index] if index < len(ids) else ""
                order = orders[index] if index < len(orders) else index + 1
                upload = request.FILES.get(f"caption_slide_image_{index + 1}")

                slide_image = existing_images.get(image_id) if image_id else CaptionSlideImage(page=page)
                slide_image.order = order or index + 1
                if upload:
                    slide_image.image = upload
                if slide_image.image:
                    slide_image.save()
                    seen_images.append(slide_image.pk)

            page.images.exclude(pk__in=seen_images).delete()
            return redirect("caption_slide_page_dashboard")
    else:
        form = CaptionSlidePageForm(instance=page)

    caption_slide_pages = CaptionSlidePage.objects.prefetch_related("images").all()
    existing_images = list(page.images.all()) if page else []
    caption_slide_image_rows = existing_images[:3] + [None] * max(0, 3 - len(existing_images))
    return render(
        request,
        "decks/caption_slide_page_dashboard.html",
        {
            "form": form,
            "page": page,
            "caption_slide_image_rows": caption_slide_image_rows,
            "caption_slide_pages": caption_slide_pages,
            "active_menu": "caption_slide",
        },
    )


def new_joiners_dashboard(request):
    page = NewJoinersPage.objects.prefetch_related("joiners").first()

    if request.method == "POST":
        form = NewJoinersPageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            existing_joiners = {str(joiner.pk): joiner for joiner in page.joiners.all()}
            seen_joiners = []

            ids = request.POST.getlist("new_joiner_id")
            names = request.POST.getlist("new_joiner_name")
            designations = request.POST.getlist("new_joiner_designation")
            orders = request.POST.getlist("new_joiner_order")

            for index in range(10):
                joiner_id = ids[index] if index < len(ids) else ""
                name = names[index].strip() if index < len(names) else ""
                designation = designations[index].strip() if index < len(designations) else ""
                order = orders[index] if index < len(orders) else index + 1
                upload = request.FILES.get(f"new_joiner_image_{index + 1}")

                joiner = existing_joiners.get(joiner_id) if joiner_id else NewJoiner(page=page)
                joiner.name = name
                joiner.designation = designation
                joiner.order = order or index + 1
                if upload:
                    joiner.image = upload
                if joiner.name and joiner.designation and joiner.image:
                    joiner.save()
                    seen_joiners.append(joiner.pk)

            page.joiners.exclude(pk__in=seen_joiners).delete()
            return redirect("new_joiners_dashboard")
    else:
        form = NewJoinersPageForm(instance=page)

    new_joiners_pages = NewJoinersPage.objects.prefetch_related("joiners").all()
    existing_joiners = list(page.joiners.all()) if page else []
    new_joiner_rows = existing_joiners[:10] + [None] * max(0, 10 - len(existing_joiners))
    return render(
        request,
        "decks/new_joiners_dashboard.html",
        {
            "form": form,
            "page": page,
            "new_joiner_rows": new_joiner_rows,
            "new_joiners_pages": new_joiners_pages,
            "active_menu": "new_joiners",
        },
    )


def promotions_dashboard(request):
    page = PromotionsPage.objects.prefetch_related("promotions").first()

    if request.method == "POST":
        form = PromotionsPageForm(request.POST, instance=page)
        if form.is_valid():
            page = form.save()
            existing_promotions = {str(promotion.pk): promotion for promotion in page.promotions.all()}
            seen_promotions = []

            ids = request.POST.getlist("promotion_id")
            names = request.POST.getlist("promotion_name")
            designations = request.POST.getlist("promotion_designation")
            orders = request.POST.getlist("promotion_order")

            for index in range(10):
                promotion_id = ids[index] if index < len(ids) else ""
                name = names[index].strip() if index < len(names) else ""
                designation = designations[index].strip() if index < len(designations) else ""
                order = orders[index] if index < len(orders) else index + 1
                upload = request.FILES.get(f"promotion_image_{index + 1}")

                promotion = existing_promotions.get(promotion_id) if promotion_id else Promotion(page=page)
                promotion.name = name
                promotion.designation = designation
                promotion.order = order or index + 1
                if upload:
                    promotion.image = upload
                if promotion.name and promotion.designation and promotion.image:
                    promotion.save()
                    seen_promotions.append(promotion.pk)

            page.promotions.exclude(pk__in=seen_promotions).delete()
            return redirect("promotions_dashboard")
    else:
        form = PromotionsPageForm(instance=page)

    promotions_pages = PromotionsPage.objects.prefetch_related("promotions").all()
    existing_promotions = list(page.promotions.all()) if page else []
    promotion_rows = existing_promotions[:10] + [None] * max(0, 10 - len(existing_promotions))
    return render(
        request,
        "decks/promotions_dashboard.html",
        {
            "form": form,
            "page": page,
            "promotion_rows": promotion_rows,
            "promotions_pages": promotions_pages,
            "active_menu": "promotions",
        },
    )


def kudos_moments_dashboard(request):
    page = KudosMomentPage.objects.prefetch_related("cards").first()

    if request.method == "POST":
        form = KudosMomentPageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            page = form.save()
            existing_cards = {str(card.pk): card for card in page.cards.all()}
            seen_cards = []

            ids = request.POST.getlist("kudos_card_id")
            values = request.POST.getlist("kudos_card_value")
            labels = request.POST.getlist("kudos_card_label")
            orders = request.POST.getlist("kudos_card_order")

            for index in range(10):
                card_id = ids[index] if index < len(ids) else ""
                value = values[index].strip() if index < len(values) else ""
                label = labels[index].strip() if index < len(labels) else ""
                order = orders[index] if index < len(orders) else index + 1

                card = existing_cards.get(card_id) if card_id else KudosMomentCard(page=page)
                card.value = value
                card.label = label
                card.order = order or index + 1
                if card.value and card.label:
                    card.save()
                    seen_cards.append(card.pk)

            page.cards.exclude(pk__in=seen_cards).delete()
            return redirect("kudos_moments_dashboard")
    else:
        form = KudosMomentPageForm(instance=page)

    kudos_pages = KudosMomentPage.objects.prefetch_related("cards").all()
    existing_cards = list(page.cards.all()) if page else []
    kudos_card_rows = existing_cards[:10] + [None] * max(0, 10 - len(existing_cards))
    return render(
        request,
        "decks/kudos_moments_dashboard.html",
        {
            "form": form,
            "page": page,
            "kudos_card_rows": kudos_card_rows,
            "kudos_pages": kudos_pages,
            "active_menu": "kudos_moments",
        },
    )


def special_appreciation_dashboard(request):
    page = SpecialAppreciationPage.objects.first()

    if request.method == "POST":
        form = SpecialAppreciationPageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect("special_appreciation_dashboard")
    else:
        form = SpecialAppreciationPageForm(instance=page)

    special_pages = SpecialAppreciationPage.objects.all()
    return render(
        request,
        "decks/special_appreciation_dashboard.html",
        {
            "form": form,
            "page": page,
            "special_pages": special_pages,
            "active_menu": "special_appreciation",
        },
    )


def kudos_bullet_moments_dashboard(request):
    page = KudosBulletMomentPage.objects.prefetch_related("cards").first()

    if request.method == "POST":
        form = KudosBulletMomentPageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            page = form.save()
            existing_cards = {str(card.pk): card for card in page.cards.all()}
            seen_cards = []

            ids = request.POST.getlist("kudos_bullet_card_id")
            card_types = request.POST.getlist("kudos_bullet_card_type")
            values = request.POST.getlist("kudos_bullet_card_value")
            labels = request.POST.getlist("kudos_bullet_card_label")
            titles = request.POST.getlist("kudos_bullet_card_title")
            contents = request.POST.getlist("kudos_bullet_card_content")
            orders = request.POST.getlist("kudos_bullet_card_order")

            for index in range(10):
                card_id = ids[index] if index < len(ids) else ""
                card_type = card_types[index] if index < len(card_types) else KudosBulletMomentCard.METRIC
                value = values[index].strip() if index < len(values) else ""
                label = labels[index].strip() if index < len(labels) else ""
                title = titles[index].strip() if index < len(titles) else ""
                content = contents[index].strip() if index < len(contents) else ""
                order = orders[index] if index < len(orders) else index + 1

                card = existing_cards.get(card_id) if card_id else KudosBulletMomentCard(page=page)
                card.card_type = card_type
                card.value = value
                card.label = label
                card.title = title
                card.content = content
                card.order = order or index + 1

                if card.value or card.label or card.title or card.content:
                    card.save()
                    seen_cards.append(card.pk)

            page.cards.exclude(pk__in=seen_cards).delete()
            return redirect("kudos_bullet_moments_dashboard")
    else:
        form = KudosBulletMomentPageForm(instance=page)

    kudos_pages = KudosBulletMomentPage.objects.prefetch_related("cards").all()
    existing_cards = list(page.cards.all()) if page else []
    kudos_card_rows = existing_cards[:10] + [None] * max(0, 10 - len(existing_cards))
    card_type_choices = KudosBulletMomentCard.CARD_TYPE_CHOICES
    return render(
        request,
        "decks/kudos_bullet_moments_dashboard.html",
        {
            "form": form,
            "page": page,
            "kudos_card_rows": kudos_card_rows,
            "kudos_pages": kudos_pages,
            "card_type_choices": card_type_choices,
            "active_menu": "kudos_bullet_moments",
        },
    )
