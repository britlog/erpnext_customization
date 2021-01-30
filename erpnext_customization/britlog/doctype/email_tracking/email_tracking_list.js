frappe.listview_settings['Email Tracking'] = {
	add_fields: ["event"],
	get_indicator: function(doc) {
		if(doc.event == "sent") {
			return [__("Sent"), "blue", "event,=,sent"];
		}
		else if(doc.event == "open") {
			return [__("Opened"), "green", "event,=,open"];
		}
		else if(doc.event == "click") {
			return [__("Clicked"), "green", "event,=,click"];
		}
		else if(doc.event == "bounce") {
			return [__("Bounced"), "red", "event,=,bounce"];
		}
		else if(doc.event == "spam") {
			return [__("Spam"), "red", "event,=,spam"];
		}
		else if(doc.event == "blocked") {
			return [__("Blocked"), "red", "event,=,blocked"];
		}
		else if(doc.event == "unsub") {
			return [__("Unsubscribed"), "orange", "event,=,unsub"];
		}
	}	
}
