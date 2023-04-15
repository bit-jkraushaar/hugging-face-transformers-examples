# hugging-face-transformers-examples
This repository contains examples for using Hugging Face's Transformers and Pipelines.

In order to execute the examples, Python is required.
All examples are tested with Python 3.10.9 under Windows 11.

## Setup

1. Install Python
2. Add the Hugging Face `transfomers` library: `pip install transfomers`
3. Install PyTorch (example uses Cuda, see [alternatives](https://pytorch.org/)): `pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117`

## Examples

### germa-qa.py

This example uses the Q&A model [deepset/gelectra-base-germanquad](https://huggingface.co/deepset/gelectra-base-germanquad).
It allows you to specify an url and a question.
The model extracts the answer and prints it to command line.

First of all you have to install the required dependencies:

```
pip install requests beautifulsoup4
```

Now you should be able to run the script:

```
> python german-qa.py https://de.wikipedia.org/wiki/Fu%C3%9Fball "Welcher Verein ging in Deutschland als erster an die Börse?"
> Borussia Dortmund (Score: 0.8863185048103333)
```

Please note the score.
It shows how likely the given answer is correct.
For instance:

```
> python german-qa.py https://de.wikipedia.org/wiki/Fu%C3%9Fball "Wer ist deutscher Rekordmeister?"
> Konrad Koch (Score: 0.07024901360273361)
```

But:

```
> python german-qa.py https://de.wikipedia.org/wiki/Fu%C3%9Fball-Bundesliga "Wer ist deutscher Rekordmeister?"
> FC Bayern München (Score: 0.7162473201751709)
```
