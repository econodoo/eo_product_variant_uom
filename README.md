# Product Variant UoM Module

## Overview

This Odoo module provides advanced UoM (Unit of Measure) conversion for sale order lines, specifically designed for products with quantity-based variant attributes.

## Features

- Captures original UoM and quantity during sale order line creation
- Automatically converts sale order lines to base UoM during order confirmation
- Maintains total price integrity during UoM conversion
- Preserves original pricing for invoicing
- Ensures correct product reporting and production tracking

## Use Case

Ideal for scenarios where:

- Products are sold in bundled quantities
- Pricing varies based on package size
- Accurate unit-level reporting is required

## Installation

1. Copy the module to your Odoo addons directory
2. Install the module through Odoo Apps or using the -u flag
3. Create a variant attribute with the name Quantity
4. Map Product with UOM in **Inventory/Configuration/Product Variant UOM**

## Technical Details

- Extends `product.product` model
- Adds `uom_id` fields
- Add views and menus to handle UoM for product

## Limitations

- Assumes consistent pricing across UoM conversions
- Requires careful configuration of product UoM and variant attributes

## Recommended Configuration

- Set up product variants with fixed quantity attributes
- Configure pricelists to reflect bundled pricing
