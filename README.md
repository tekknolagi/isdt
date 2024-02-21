# Introduction to Software Development Tooling

Hello and welcome to the repository containing the website for our course. We
figured since we were teaching about version control, we might as well open up
the course website on GitHub.

If you are a student in the course, you are likely looking for (or came from)
the [compiled HTML site](https://bernsteinbear.com/isdt/). Please
consider that (or the latest commit) the source of truth.

Issues and Pull Requests are primarily intended for use by course staff but if
you discover something glaring or would like to make a contribution, please go
ahead and file something.

## How to build locally

1. Install `rbenv` and `ruby-build`
   1. `mkdir -p "$(rbenv root)"/plugins`
   1. `git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build`
1. `rbenv install 3.3.0`  or `mise install ruby@3.3` and `mise use ruby@3.3`
   (maybe it works fine with `.mise.toml` and you don't need `use`)
1. `bundle install`
1. `bundle exec jekyll serve --watch`
