odoo.define("my_library.counter", function (require) {
  const AbstractAction = require("web.AbstractAction");
  const Widget = require("web.Widget");
  const core = require("web.core");

  // Extend the AbstractAction (base class) to define our own template
  const QuizAction = AbstractAction.extend({
    template: "my_library.ClientAction",
    start() {
      const counter = new Counter(this, 47);
      counter.appendTo(this.$el);
    },
  });

  // Create the Counter widget by extending the default web widget.
  const Counter = Widget.extend({
    template: "my_library.Counter",
    events: {
      "click .increment": "increment",
    },
    init(parent, initialValue) {
      this._super(parent);
      this.value = initialValue;
    },
    increment() {
      this.value++;
      this.$el.find("span.o-value").text(this.value);
    },
  });

  core.action_registry.add("my_library.action", QuizAction);
});
