[![PyPI version](https://badge.fury.io/py/ghicon.svg)](https://badge.fury.io/py/ghicon)

# ghicon
**ghicon** is a GitHubesque identicon generator. It uses seed text and a hashing function, [MD5](https://en.wikipedia.org/wiki/MD5) by default, to create unique images called [identicons](https://en.wikipedia.org/wiki/Identicon).

## Usage
Install **ghicon** using,
```
pip install ghicon==5.2.0
```

Then use the `generate` function,
```py
import ghicon

image = ghicon.generate("agzg")
image.save("agzg.png")
```

**Note:** Following `v5.2.0`, you can supply and use custom hashing functions for generating identicons. Ensure the function you use only accepts a string and returns a hex-compatible hash which is more than 15 characters.

**Tip:** You can also invert the colours of the identicon to mix things up! Use the `invert` argument to do so.

## Examples
<p align="center">
	<img src="https://raw.githubusercontent.com/agzg/ghicon/372e7324bf64a3ab2d191eb01cb818410f579ee8/examples/a.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/372e7324bf64a3ab2d191eb01cb818410f579ee8/examples/b.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/372e7324bf64a3ab2d191eb01cb818410f579ee8/examples/c.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/372e7324bf64a3ab2d191eb01cb818410f579ee8/examples/d.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/372e7324bf64a3ab2d191eb01cb818410f579ee8/examples/e.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/372e7324bf64a3ab2d191eb01cb818410f579ee8/examples/f.png" width="128"/>&nbsp;
</p>

## License
Governed under the [MIT license](https://github.com/agzg/ghicon/blob/main/LICENSE).
