# 🥯 Bunji - TUI Expense Tracker

Powerful expense tracker that lives in your terminal.

![PyPI - Version](https://img.shields.io/pypi/v/bunji?style=for-the-badge)
![GitHub License](https://img.shields.io/github/license/radityprtama/Bunji?style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/Bunji?style=for-the-badge)

<!-- <a title="This tool is Tool of The Week on Terminal Trove, The $HOME of all things in the terminal" href="https://terminaltrove.com/bunji"><img src="https://cdn.terminaltrove.com/media/badges/tool_of_the_week/svg/terminal_trove_tool_of_the_week_black_on_white_bg.svg" alt="Terminal Trove Tool of The Week" height="28" /></a> -->

![Bunji](./public/screenshots/thumb1.png)
![Bunji](./public/screenshots/thumb2.png)

Bunji expense tracker is a TUI application where you can track and analyse your money flow, with convenience oriented features and a complete interface.

> **Why an expense tracker in the terminal?**
> I found it easier to build a habit and keep an accurate track of my expenses if I do it at the end of the day, instead of on the go. So why not in the terminal where it's fast, and I can keep all my data locally?

## ✨ Features

Some notable features include:

- Accounts, (Sub)Categories, Splits, Transfers, Records
- Templates for Recurring Transactions
- Add Templated Record with Number Keys
- Clear Table Layout with Togglable Splits
- Transfer to and from Outside Tracked Accounts
- "Jump Mode" Navigation
- Less and Less Fields to Enter per Transaction, Powered by Transactions and Input Modes
- Insights
- Customizable Keybindings and Defaults, such as First Day of Week
- Label, amount and category filtering
- Spending plottings / graphs with estimated spendings
- Budgetting tool for saving money and limiting unnecessary spendings

## 📦 Installation

<details open>
    <summary><b>Recommended: By UV</b></summary>

Bunji can be installed via uv on MacOS, Linux, and Windows.

`uv` is a single Rust binary that you can use to install Python apps. It's significantly faster than alternative tools, and will get you up and running with Bunji in seconds.

You don't even need to worry about installing Python yourself - uv will manage everything for you.

#### Unix / MacOS:

```bash
# install uv (package manager):
curl -LsSf https://astral.sh/uv/install.sh | sh

# restart your terminal, or run the following command:
source $HOME/.local/bin/env # or follow instructions

# install bunji through uv
uv tool install --python 3.13 bunji
```

`uv` can also be installed via Homebrew, Cargo, Winget, pipx, and more. See the [installation guide](https://docs.astral.sh/uv/getting-started/installation/) for more information.

#### Windows:

```bash
# install uv:
winget install --id=astral-sh.uv  -e
# then follow instructions to add uv to path
uv tool install --python 3.13 bunji
```

</details>

<details>
    <summary>By Brew</summary>

    brew install bunji

</details>

<details>
    <summary>By Pipx</summary>

    pipx install bunji

</details>

<details>
    <summary>By Conda</summary>

    conda install -c conda-forge bunji

</details>

<details>
    <summary>By X-CMD</summary>

    x install bunji

</details>

## 🥯 Usage:

```bash
bunji # start bunji
bunji --at "./" # start bunji with data stored at cd
bunji locate database # find database file path
bunji locate config # find config file path
```

> It is recommended, but not required, to use "modern" terminals to run the app. MacOS users are recommended to use Ghostty, and Windows users are recommended to use Windows Terminal.

To upgrade with uv:

```bash
uv tool upgrade bunji
```

## ↔️ Migration

Please read the [migration guide](MIGRATION.md) for migration from other services.

## 🛠️ Development setup

```sh
git clone https://github.com/radityprtama/Bunji.git
cd Bunji
uv run pre-commit install
mkdir instance
uv run bunji --at "./instance/" # runs app with storage in ./instance/
# alternatively, use textual dev mode to catch prints
uv run textual run --dev "./src/bunji/textualrun.py"
uv run textual console -x SYSTEM -x EVENT -x DEBUG -x INFO # for logging
```

Please use the black formatter to format the code.

## 🗺️ Roadmap

- [x] Budgets (Major!)
- [x] More insight displays and analysis (by nature etc.)
- [ ] Daily check-ins
- [ ] Pagination for records on monthly and yearly views.
- [ ] Importing from various formats

Backlog:

- [ ] "Processing" bool on records for transactions in process
- [ ] Record flags for future insights implementation
- [ ] Code review
- [ ] Repayment reminders
- [ ] Add tests
- [ ] Bank sync

## Attributions

- Heavily inspired by [posting](https://posting.sh/)
- Bunji is built with [textual](https://textual.textualize.io/)
