$.extend(cur_frm.cscript, {
    onload: function (doc, dt, dn) {

        if (!doc.status) doc.status = 'New';
        cfn_set_buttons(doc, dt, dn);
    },

    refresh: function(doc, dt, dn) {
        this.frm.dashboard.reset();
        cfn_set_buttons(doc, dt, dn);
        var percent = doc.spent_time/doc.planned_time*100
        this.frm.dashboard.add_progress(cint(percent) + "% " + __("Complete"), percent);
    }
});

var cfn_set_buttons = function(doc, dt, dn) {

    if (doc.status == 'New' && user_roles.indexOf("Manufacturing User")!=-1){
        cur_frm.add_custom_button(__('Start'),
            cur_frm.cscript['Start'], 'icon-play');
    }

    if (doc.status == 'In Progress' && user_roles.indexOf("Manufacturing User")!=-1){
        cur_frm.add_custom_button(__('Finish'),
            cur_frm.cscript['Finish'], 'icon-ok');
        cur_frm.add_custom_button(__('Pending'),
            cur_frm.cscript['Pending'], 'icon-pause');                      
    }

    if (doc.status == 'Pending' && user_roles.indexOf("Manufacturing User")!=-1){
        cur_frm.add_custom_button(__('Reopen'),
            cur_frm.cscript['Start'], 'icon-undo');            
    }            
}

cur_frm.cscript['Start'] = function() {
    return frappe.call({
        doc: cur_frm.doc,
        method: "set_in_progress",
        callback: function(r) {
            if(!r.exc) cur_frm.refresh();
        }
    }) 
}

cur_frm.cscript['Finish'] = function() {
    return frappe.call({
        doc: cur_frm.doc,
        method: "set_complete",
        callback: function(r) {
            if(!r.exc) cur_frm.refresh();
        }
    }) 
}

cur_frm.cscript['Pending'] = function() {
    return frappe.call({
        doc: cur_frm.doc,
        method: "set_pending",
        callback: function(r) {
            if(!r.exc) cur_frm.refresh();
        }
    }) }