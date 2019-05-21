from modelcluster.fields import ParentalManyToManyField
from modelcluster.models import ClusterableModel
from django.utils.translation import ugettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PublishingPanel

from wagtail_tag_manager.models import Tag
from wagtail_tag_manager.widgets import (
    HorizontalCheckboxSelectMultiple as CheckboxSelectMultiple,
)


class TagMixin(ClusterableModel):
    tags = ParentalManyToManyField(
        Tag,
        related_name="pages",
        help_text=_("The tags to include when this page is loaded."),
    )

    settings_panels = [
        PublishingPanel(),
        MultiFieldPanel(
            [FieldPanel("tags", widget=CheckboxSelectMultiple)], heading=_("Tags")
        ),
    ]

    class Meta:
        abstract = True
