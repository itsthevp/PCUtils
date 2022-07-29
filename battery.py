from asyncio import run, sleep
from psutil import sensors_battery

from popup import popup


def _check_battery_percentages(low: int, high: int):
    battery = sensors_battery()

    if battery.power_plugged is None:
        return "No Battery Installed !!"

    percent = battery.percent

    if percent < low and not battery.power_plugged:
        return popup(
            title="Low Battery",
            message=f"Current battery percentage is lower than {low}\nIt's a time to plugin the charger !!",
        )

    if percent > high and battery.power_plugged:
        return popup(
            title="Battery Charged",
            message=f"Current battery percentage is higher than {high}\nPlease unplug the charger !!",
        )


def start_monitoring_battery(low: int, high: int, interval: float):
    """
    Monitors the battery
    :param low: Lowest percentage after which charger needs to be plugged in
    :param high: Highest percentage after which charger needs to be plugged out
    :param interval: after amount of every these many seconds check battery status
    """

    async def monitor_battery():
        while True:
            _check_battery_percentages(low, high)
            await sleep(delay=interval)

    try:
        if not 0 < low < high:
            raise ValueError("Invalid Thresholds !!")

        run(monitor_battery())

    except (Exception, KeyboardInterrupt) as e:
        return popup(
            title="Alert",
            message=f"Battery Monitoring Stopped\nReason: {str(e) or 'Keyboard Interrupt !!'}",
        )


if __name__ == "__main__":
    # Let's start monitoring
    start_monitoring_battery(low=20, high=80, interval=300)
