[![PyPI version](https://badge.fury.io/py/ghicon.svg)](https://badge.fury.io/py/ghicon)

# ghicon
**ghicon** is a GitHubesque identicon generator. It uses seed text and a hashing function, [MD5](https://en.wikipedia.org/wiki/MD5) by default, to create unique icons called [identicons](https://en.wikipedia.org/wiki/Identicon).

## Usage
Install **ghicon** using,
```
pip install ghicon==5.2.2
```

Then use the `generate` function,
```py
import ghicon

image = ghicon.generate("agzg")
image.save("agzg.png")
```

**Note:** Following `v5.2.0`, you can use custom hashing functions to generate identicons via the `hasher` argument. Ensure the function you use only accepts a single string argument and returns a hexadecimal string hash longer than 15 characters.

**Tip:** You can also invert the colours of the identicon to mix things up! Use the `invert` argument to do so.

## Examples
<p align="center">
	<img src="https://raw.githubusercontent.com/agzg/ghicon/994529aaf83647e189ab6abb0550256ab2163896/examples/a.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/994529aaf83647e189ab6abb0550256ab2163896/examples/b.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/994529aaf83647e189ab6abb0550256ab2163896/examples/c.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/994529aaf83647e189ab6abb0550256ab2163896/examples/d.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/994529aaf83647e189ab6abb0550256ab2163896/examples/e.png" width="128"/>&nbsp;
</p>

## License
Governed under the [MIT license](https://github.com/agzg/ghicon/blob/main/LICENSE).
