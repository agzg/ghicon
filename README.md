# ghicon
**ghicon** is a GitHubesque identicon generator. It uses the seed text and the cryptographic hash function, [MD5](https://en.wikipedia.org/wiki/MD5), to create unique images called [identicons](https://en.wikipedia.org/wiki/Identicon).

## Usage
Install **ghicon** using,
```
pip install ghicon
```

Then use the `generate` function,
```py
import ghicon

image = ghicon.generate("agzg")
image.save("agzg.png")
```

**Tip:** You can also invert the colours of the identicon to mix things up! 

## Examples
<p align="center">
	<img src="https://raw.githubusercontent.com/agzg/ghicon/372e7324bf64a3ab2d191eb01cb818410f579ee8/examples/a.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/372e7324bf64a3ab2d191eb01cb818410f579ee8/examples/b.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/372e7324bf64a3ab2d191eb01cb818410f579ee8/examples/c.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/372e7324bf64a3ab2d191eb01cb818410f579ee8/examples/d.png" width="128"/>&nbsp;
	<img src="https://raw.githubusercontent.com/agzg/ghicon/372e7324bf64a3ab2d191eb01cb818410f579ee8/examples/e.png" width="128"/>&nbsp;
</p>

## License
Governed under the [MIT license](https://github.com/agzg/ghicon/blob/main/LICENSE).
