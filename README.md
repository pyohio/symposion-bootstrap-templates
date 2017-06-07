# symposion-bootstrap-templates
Provides some customisable bootstrap templates for things in Symposion, so that you get basic behaviour automatically.

## What is the point of this?

`registrasion` provides a bunch of django views that make the app tick. As new features get added, so will this package. By keeping this package up to date, you'll get a default template for each new view that gets added.


## How does it work

For each template required by registrasion, `registrasion_templates` provides two templates. Say the template used by the view is called `view.html`. We provide:

* `view.html`, which is the template that is loaded directly -- this will be *very* modular, and will let you easily override things that you need to override in your own installations
* `view_.html`, which is the thing that lays everything out.

So you can either override `view_.html` if you're happy with the text and markup that `view.html` provides, or you can override `view.html` if you want to change the entire thing. Your choice!


## Installation

Ensure that `APP_DIRS` is switched on in your `settings`, like so:

```
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
}]
```

Then add `registration_templates` to your INSTALLED_APPS:

```
INSTALLED_APPS = [
  ...
  "registrasion_templates",
  ...
]
```


### Overriding our defaults:

* `registrasion/form.html` is used by these templates whenever a form needs to be rendered. The default implementation of this just calls ``{form}``.
* `registrasion/base.html` extends `site_base.html`. Each `view_.html` template that we provide extends `registrasion/base.html`


## Using the templates

* Our default templates place their content in a block called `content`. Your `registrasion/base.html` MUST include a block called `content` where you want the content to appear.
* Each template will document the purpose of the templates
