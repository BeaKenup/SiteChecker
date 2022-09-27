import argparse

def read_user_cli_args():
    parser = argparse.ArgumentParser(
        prog="sitechecker", description="Teste a disponibilidade de uma URL"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="insira um ou mais URLs",
    )
    return parser.parse_args()
    
def display_check_result(result, url, error=""):
    print(f' "{url}" -', end=" ")
    if result:
        print("Site está Online!")
    else:
        print(f"Site está Offline!")