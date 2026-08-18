#!/usr/bin/env python3

# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 The Linux Foundation

"""Python wrapper for the sample/test Typer application."""

import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def hello(name: str):
    """Greets somebody."""
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    """Says goodbye."""
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")
