# examples/example_get_ndvi_poly.py

import argparse
import ee
from landsatndvi.gee_interface import initialize_gee
from landsatndvi.ndvi import get_ndvi

def main():
    parser = argparse.ArgumentParser(
        description="Get NDVI value for a predefined polygon and date range using the LandsatNDVI package."
    )
    parser.add_argument(
        "--project",
        type=str,
        required=True,
        help="The GEE project ID."
    )
    parser.add_argument(
        "--start_date",
        type=str,
        required=True,
        help="Start date in format YYYY-MM-DD."
    )
    parser.add_argument(
        "--end_date",
        type=str,
        required=True,
        help="End date in format YYYY-MM-DD."
    )

    args = parser.parse_args()

    initialize_gee(project=args.project)

    # Example polygon (adjust if needed)
    coords = [
        [-83.52400783729342, 35.6839165229363],
        [-83.52400783729342, 35.66606729615823],
        [-83.50117687415866, 35.66606729615823],
        [-83.50117687415866, 35.6839165229363]
    ]
    poly = ee.Geometry.Polygon([coords])

    result = get_ndvi(poly, args.start_date, args.end_date)

    print("NDVI Result for Polygon:")
    print(result.getInfo())

if __name__ == "__main__":
    main()