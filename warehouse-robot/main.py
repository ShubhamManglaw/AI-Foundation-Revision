from warehouse.grid import WarehouseGrid


def main():

    warehouse = WarehouseGrid(15, 15)

    warehouse.add_shelf(
        start_row=2,
        start_col=3,
        height=3,
        width=5
    )

    warehouse.display()


if __name__ == "__main__":
    main()