# Stori-QA-Automation-Challenge

## Installation

  To install the required packages, run the following command:
  
  ```bash
  pip install -r requirements.txt

## Configuration

Update your device information in features/environment.py:

```bash
	    options.platform_name = "{os}"
    	options.platform_version = "{version}"
    	options.device_name = "{name_device}"

## Usage
To run the tests without generating a report:

```bash
behave 

To generate an HTML report, use the following command:

```bash
behave -f html-pretty -o reports/behave-report.html

To generate an XML report, use the command:

```bash
behave --junit 

To run a specific scenario using tags:

```bash
behave -t "@{name_tag}" 
