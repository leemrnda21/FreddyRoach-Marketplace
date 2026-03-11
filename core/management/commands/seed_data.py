from pathlib import Path

from django.core.management import BaseCommand, CommandError, call_command


class Command(BaseCommand):
    help = "Load seed data fixture with safe encoding handling."

    def handle(self, *args, **options):
        fixture_path = Path("fixtures/seed.json")
        if not fixture_path.exists():
            raise CommandError("Missing fixtures/seed.json. Run dumpdata or add the fixture.")

        self._normalize_fixture_encoding(fixture_path)
        call_command("loaddata", str(fixture_path))
        self.stdout.write(self.style.SUCCESS("Seed data loaded."))

    def _normalize_fixture_encoding(self, fixture_path: Path) -> None:
        raw = fixture_path.read_bytes()

        try:
            raw.decode("utf-8")
            return
        except UnicodeDecodeError:
            pass

        for encoding in ("utf-8-sig", "cp1252", "latin-1"):
            try:
                text = raw.decode(encoding)
                fixture_path.write_text(text, encoding="utf-8")
                return
            except UnicodeDecodeError:
                continue

        raise CommandError("Unable to normalize fixture encoding.")
