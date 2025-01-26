"""Console script for meboot."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("meboot")
    click.echo("=" * len("meboot"))
    click.echo("Maximum Entropy Bootstrap for timeseries")


if __name__ == "__main__":
    main()  # pragma: no cover
