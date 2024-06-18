# degiro-trading-tracker

Simplified tracking of your [Degiro](https://www.degiro.com) investments by getting quick overview of total: 

* amount invested in stocks
* gains from sold stocks
* fee costs. 

by automatically analyzing exported `.xls` transactions file and performing caculations on your behalf.

Example output with dummy data:

<img src="https://foolcontrol.org/wp-content/uploads/2020/11/degiro-trading-tracker-example-output.jpg" width="550" />

If you're interested in opening Degiro account and earning 20€ credit, please [follow this link](https://www.degiro.nl/start-met-beleggen?id=25367010&amp;utm_source=mgm).


## Why do I need degiro-trading-tracker?

If you bought or sold more then few stocks with Degiro, it's tedious and hard to keep track of exact amount of money which was invested, or amount which was spent in fees. As each time you want to check one of these, you'll need to export Degiro "Transactions" `.xls` file, open it with Microsoft Excel/LibreOffice Calc and then do the calculations yourself.

This tool allows you to automatically display data of interest without even opening the `.xls` file.

## How to run degiro-trading-tracker

### Requirements

Python 3 and necessary libraries. After Python3 is installed, necessary libarires can be installed by running:
```
pip3 install pandas numpy xlrd
python3 degiro-trading-tracker.py
```

Or by using `pipenv`:

```
pipenv install
pipenv shell
python degiro-trading-tracker.py
```


### Running degiro-trading-tracker

#### 1. Download Degiro Transactions file

Under "Overzichten", select "Transacties" and pick desired date range and click "Export", i.e:
<img src="https://foolcontrol.org/wp-content/uploads/2020/11/degiro-transactions-export.jpg" width="800" />

*Make sure file is exported as .xls*

#### 2. Run degiro-trading-tracker

Run degiro-trading-tracker by pointing it to exported `.xls` file, i.e:

```
python3 degiro-trading-tracker.py ~/Downloads/Transactions.xls
```

#### Limitations

Currently:

* exported transactions file must be in Dutch
* only supported file format for exported transaction file is `.xls`

If you'd like me to add support for your language, or have some other idea or a problem, please [submit an issue or feature request](https://github.com/AdnanHodzic/degiro-trading-tracker/issues).

## Discussion:

* Blogpost: [Degiro trading tracker - Simplified tracking of your investments](http://foolcontrol.org/?p=3614)

## Donate

If you found this tool useful, please consider supporting the project by making a donation of any amount!

##### Become Github Sponsor

[Become a sponsor to Adnan Hodzic on Github](https://github.com/sponsors/AdnanHodzic) to acknowledge my efforts and help project's further open source development.

#### PayPal
[![paypal](https://www.paypalobjects.com/en_US/NL/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=adnan%40hodzic.org&item_name=Purpose%3A+Contribution+for+work+on+degiro-trader-tracker&currency_code=EUR)

#### BitCoin
[bc1qlncmgdjyqy8pe4gad4k2s6xtyr8f2r3ehrnl87](bitcoin:bc1qlncmgdjyqy8pe4gad4k2s6xtyr8f2r3ehrnl87)

[![bitcoin](https://foolcontrol.org/wp-content/uploads/2019/08/btc-donate-displaylink-debian.png)](bitcoin:bc1qlncmgdjyqy8pe4gad4k2s6xtyr8f2r3ehrnl87)
