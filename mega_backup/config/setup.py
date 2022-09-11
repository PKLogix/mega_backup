from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Integrations"),
            "icon": "octicon octicon-cloud-upload",
            "items": [
                {
                    "type": "doctype",
                    "name": "Mega Settings",
                    "label": _("Mega Backup"),
                    "description": _("Mega Backup for Frappe and ERPNext"),
                    "hide_count": True
                }
            ]
        }
    ]
