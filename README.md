# anyser

Common interfaces for multiple serialization formats.

## API

- `load(o: str|bytes|IOBase, format: str, **options) -> object`
- `loads(s: str, format: str, **options) -> object`
- `loadb(b: bytes, format: str, **options) -> object`
- `loadf(f: IOBase, format: str, **options) -> object`
- `dumps(obj, format: str, **options) -> str`
- `dumpb(obj, format: str, **options) -> bytes`
- `dumpf(obj, fp: IOBase, format: str, **options) -> None`

format canbe:

| Format | Data format             | requires                |
|:-------|:------------------------|:------------------------|
| json   | `json`, `.json`         |                         |
| pickle | `pickle`                |                         |
| xml    | `xml`, `.xml`           |                         |
| json5  | `json5`, `.json5`       | install `anyser[json5]` |
| toml   | `toml`, `.toml`         | install `anyser[toml]`  |
| yaml   | `yaml`, `.yaml`, `.yml` | install `anyser[yaml]`  |

### Options

- `origin_kwargs: dict` - the dict pass to the base serializer.
- `ensure_ascii: bool` - default `True`; for all `dump*` api.
- `indent: int` - default `None`; for all `dump*` api.
- `size_limit: int` - limit size to read, only for `loadf`; if the `IOBase` has more data, raise `SizeOverflowError`.
