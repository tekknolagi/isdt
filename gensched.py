import datetime


def link(name, url):
    return f"[{name}]({{{{site.baseurl}}}}/{url})"


def lecture(name, notes, slides=None):
    if slides:
        return link(name, notes) + " (" + link("slides", slides) + ")"
    if notes.endswith(".pdf"):
        return link(f"{name} (pdf)", notes)
    return link(name, notes)


material = iter(
    [
        [
            "Course Administrivia &amp; "
            + lecture(
                "CLI 1: Intro to Linux and the shell", "lecture-notes/1-cli/#lecture-1"
            ),
            link("Homework 1 out", "assignments/01-cli-investigative/"),
        ],
        [
            lecture(
                "CLI 2: Quoting, common tools, and permissions",
                "lecture-notes/1-cli/#lecture-2",
            ),
        ],
        [
            lecture("CLI 3: Advanced shell features", "lecture-notes/1-cli/#lecture-3"),
        ],
        [
            lecture(
                "CLI 4: The shell as a programming language",
                "lecture-notes/1-cli/#lecture-4",
            ),
            "Homework 1 due; "
            + link("Homework 2 out", "assignments/02-cli-constructive/"),
        ],
        [
            lecture("CLI 5: Behind the scenes", "lecture-notes/1-cli/#lecture-5"),
        ],
        [lecture("CLI 6: Linux and POSIX", "lecture-notes/1-cli/#lecture-6")],
        [
            lecture(
                "VCS 1: Intro to version control", "lecture-notes/2-vcs/#lecture-1"
            ),
            "Homework 2 due; "
            + link("Homework 3 out", "assignments/03-vcs-investigative/"),
        ],
        [
            lecture("VCS 2: Git operations", "lecture-notes/2-vcs/#lecture-2"),
        ],
        [
            "VCS 3: Git operations, continued",
        ],
        [
            lecture("VCS 4: Git operations, continued", "lecture-notes/2-vcs/#lecture-4"),
            "Homework 3 due; "
            + link("Homework 4 out", "assignments/04-vcs-constructive/"),
        ],
        [
            lecture(
                "VCS 5: Collaboration with Git",
                "lecture-notes/2-vcs-slides-l5.pdf",
            ),
        ],
        [
            lecture(
                "VCS 6: Survey of alternative and related tools",
                "lecture-notes/2-vcs-slides-l6.pdf",
            ),
        ],
        [
            lecture(
                "BLD 1: Intro to build systems",
                "lecture-notes/3-bld/#lecture-1",
                "lecture-notes/3-bld-slides-l1.pdf",
            ),
            "Homework 4 due; "
            + link("Homework 5 out", "assignments/05-bld-investigative/"),
        ],
        [
            lecture(
                "BLD 2: Intro to Make",
                "lecture-notes/3-bld/#lecture-2",
                "lecture-notes/3-bld-slides-l2.pdf",
            )
        ],
        [
            lecture("BLD 3: The Make language", "lecture-notes/3-bld-slides-l3.pdf"),
        ],
        [
            lecture(
                "BLD 4: Compilation and linking + large-scale Make",
                "lecture-notes/3-bld-slides-l4.pdf",
            ),
            "Homework 5 due; "
            + link("Homework 6 out", "assignments/06-bld-constructive/"),
        ],
        [
            lecture("BLD 5: The great wide world", "lecture-notes/3-bld-slides-l5.pdf"),
            link("Graph lab", "build-lab/"),
        ],
        [
            lecture(
                "BLD 6: The great wide world, continued",
                "lecture-notes/3-bld-slides-l6.pdf",
            ),
        ],
        [
            lecture(
                "COR 1: Intro to software correctness",
                "lecture-notes/4-cor/#lecture-1",
                "lecture-notes/4-cor-slides-l1.pdf",
            ),
            "Homework 6 due; "
            + link("Homework 7 out", "assignments/07-cor-investigative/"),
        ],
        [
            lecture(
                "COR 2: Philosophy of software testing",
                "lecture-notes/4-cor/#lecture-2",
                "lecture-notes/4-cor-slides-l2.pdf",
            ),
        ],
        [
            lecture(
                "COR 3: Writing unit tests",
                "lecture-notes/4-cor/#lecture-3",
                "lecture-notes/4-cor-slides-l3.pdf",
            )
        ],
        [
            lecture(
                "COR 4: Testing strategies and dependency injection",
                "lecture-notes/4-cor/#lecture-4",
                "lecture-notes/4-cor-slides-l4.pdf",
            ),
            "Homework 7 due; "
            + link("Homework 8 out", "assignments/08-cor-constructive/"),
        ],
        [
            lecture(
                "COR 5: Continuous integration", "lecture-notes/4-cor-slides-l5.pdf"
            ),
        ],
        [
            lecture(
                "COR 6: Other methods for ensuring software correctness",
                "lecture-notes/4-cor-slides-l6.pdf",
            ),
        ],
        ["TBD"],
        ["TBD", "Homework 8 due"],
        ["TBD"],
        ["TBD"],
        ["TBD"],
        ["TBD"],
        ["TBD"],
        ["TBD"],
        ["TBD"],
        ["TBD"],
    ]
)


holidays = {
    datetime.date(2024, 7, 4),  # Independence day
}
start_date = datetime.date(2024, 7, 1)
end_date = datetime.date(2024, 8, 20)
meeting_days = ["Monday", "Tuesday", "Wednesday", "Thursday"]


def fmt(date):
    cal = f"*{date.strftime('%b')} {date.day}*"
    if date in holidays:
        return f"{cal}<br>*No class*"
    try:
        return f"{cal}<br>{'<br>'.join(next(material))}"
    except StopIteration:
        return f"{cal}<br>*No class*"


weekno = 1
headings = ["Week", *meeting_days]
print(f"<!-- @@generated by {__file__} -->")
print()
print("|", " | ".join(headings), "|")
print("|", " | ".join("-" * len(heading) for heading in headings), end=" |\n")
while start_date <= end_date:
    day_of_week = start_date.strftime("%A")
    if day_of_week == meeting_days[0]:
        print("| ", weekno, end="   ")
    if day_of_week in meeting_days:
        print("|", fmt(start_date), end=" ")
    if day_of_week == meeting_days[-1]:
        weekno += 1
        print("|")
    start_date += datetime.timedelta(days=1)
try:
    x = next(material)
    if x != ["TBD"]:
        print()
        print("**Warning: ran out of space for material!**")
except StopIteration:
    pass
