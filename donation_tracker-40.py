# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: DonationTracker
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="DonationTracker CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_sub(sub_name, func):
        sp = sub.add_parser(sub_name, help=func.__doc__)
        sp.set_defaults(func=func)
        return sp

    add_sub("donor", add_donor)
    add_sub("goal", add_goal)
    add_sub("donation", add_donation)
    add_sub("report", add_report)

    def add_donor(sp):
        sp.add_argument("--name", required=True)
        sp.add_argument("--email", default="")
    def add_goal(sp):
        sp.add_argument("--name", required=True)
        sp.add_argument("--target", type=float, required=True)
    def add_donation(sp):
        sp.add_argument("--donor", required=True)
        sp.add_argument("--goal", required=True)
        sp.add_argument("--amount", type=float, required=True)
        sp.add_argument("--date", default="")
    def add_report(sp):
        sp.add_argument("--summary", action="store_true")
        sp.add_argument("--donor", default="")
        sp.add_argument("--goal", default="")

    return parser.parse_args()

def main():
    args = parse_args()
    if args.command == "donor":
        from donation_tracker import add_donor as _add
        _add(args.name, args.email)
    elif args.command == "goal":
        from donation_tracker import add_goal as _add
        _add(args.name, args.target)
    elif args.command == "donation":
        from donation_tracker import add_donation as _add
        _add(args.donor, args.goal, args.amount, args.date)
    elif args.command == "report":
        from donation_tracker import print_report
        print_report(args.summary, args.donor, args.goal)

if __name__ == "__main__":
    main()
