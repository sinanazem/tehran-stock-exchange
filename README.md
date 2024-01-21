<div>
    <img src="https://cdni.iconscout.com/illustration/premium/thumb/stock-market-growth-5788121-4849094.png?f=webp" alt="Nobel Prize" width="350" align="left" hspace="10">
    
</div>


## Tehran Stock Exchange Data Pipeline Project
This project focuses on creating a data pipeline to crawl the watchlist data from the Tehran Stock Exchange (TSE), transforming it, and loading it into a data lake for further analysis. The pipeline is designed to automate the process of collecting stock data, ensuring it is structured appropriately, and making it readily available for analytical purposes.
<br><br><br><br><br><br><br>
## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Crawling Data](#crawling-data)
  - [Transforming Data](#transforming-data)
  - [Loading Data into Data Lake](#loading-data-into-data-lake)
  - [Analysis](#analysis)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before running the project, ensure you have the following installed:

- Python (version x.x.x)
- Pip (package manager)
- [Additional prerequisites]

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sinanazem/tehran-stock-exchange.git
    cd tehran-stock-exchange
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Export PYTHONPATH

run the following command:

```bash
export PYTHONPATH=${PWD}
```

### Crawl

run the following command:

```bash
python src/run.py --startdate 1402-07-01 --enddate 1402-07-10  --delete "True"
```

## Configuration

Customize the project configuration in the `config.yaml` file. Adjust parameters such as API keys, data storage locations, and any other relevant settings.

## Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, please open an issue or submit a pull request.

---

Feel free to modify and expand this template based on the specifics of your project. Add more details about the data lake structure, analysis methods, and any other relevant information.
