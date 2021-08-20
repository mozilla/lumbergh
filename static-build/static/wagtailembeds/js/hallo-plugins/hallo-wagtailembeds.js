// Generated by CoffeeScript 1.6.2
(function() {
    (function($) {
        return $.widget('IKS.hallowagtailembeds', {
            options: {
                uuid: '',
                editable: null
            },
            populateToolbar: function(toolbar) {
                var button, widget;

                widget = this;
                button = $('<span class="' + this.widgetName + '"></span>');
                button.hallobutton({
                    uuid: this.options.uuid,
                    editable: this.options.editable,
                    label: 'Embed',
                    icon: 'icon-media',
                    command: null
                });

                toolbar.append(button);

                return button.on('click', function(event) {
                    var insertionPoint, lastSelection;

                    lastSelection = widget.options.editable.getSelection();
                    insertionPoint = $(lastSelection.endContainer).parentsUntil('[data-hallo-editor]').last();

                    return ModalWorkflow({
                        url: window.chooserUrls.embedsChooser,
                        onload: global.EMBED_CHOOSER_MODAL_ONLOAD_HANDLERS,
                        responses: {
                            embedChosen: function(embedData) {
                                var elem;

                                elem = $(embedData).get(0);
                                lastSelection.insertNode(elem);
                                if (elem.getAttribute('contenteditable') === 'false') {
                                    insertRichTextDeleteControl(elem);
                                }

                                return widget.options.editable.element.trigger('change');
                            }
                        }
                    });
                });
            }
        });
    })(jQuery);

}).call(this);
