# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: DonationTracker
import json
from datetime import datetime

def export_report_json(report):
    """Export donation report to JSON format."""
    today = datetime.now().strftime("%Y-%m-%d")
    output = {
        "report_date": today,
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "total_donations": report["total_donations"],
            "total_donors": report["total_donors"],
            "total_targets": report["total_targets"],
            "total_raised": report["total_raised"],
            "total_goal": report["total_goal"],
            "progress": round(report["progress"] * 100, 2)
        },
        "top_donors": report["top_donors"][:5],
        "targets_status": report["targets_status"]
    }
    with open("donation_report.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Report exported to donation_report.json")
    return output

def export_report_text(report):
    """Export donation report to plain text format."""
    today = datetime.now().strftime("%Y-%m-%d")
    lines = [
        "=" * 50,
        f"  DONATION TRACKER REPORT",
        f"  Generated: {today}",
        "=" * 50,
        "",
        f"  Total Donations: {report['total_donations']:,} RUB",
        f"  Total Donors: {report['total_donors']:,}",
        f"  Total Targets: {report['total_targets']:,}",
        f"  Total Raised: {report['total_raised']:,} RUB",
        f"  Total Goal: {report['total_goal']:,} RUB",
        f"  Progress: {round(report['progress'] * 100, 2)}%",
        "",
        "  TOP 5 DONORS:",
    ]
    for donor in report["top_donors"][:5]:
        lines.append(f"    - {donor['name']}: {donor['total']:,} RUB")
    lines.append("")
    lines.append("  TARGETS STATUS:")
    for target in report["targets_status"]:
        lines.append(f"    - {target['name']}: {target['raised']:,}/{target['goal']:,} RUB ({round(target['progress']*100, 1)}%)")
    lines.append("=" * 50)
    text = "\n".join(lines)
    with open("donation_report.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Report exported to donation_report.txt")
    return text
