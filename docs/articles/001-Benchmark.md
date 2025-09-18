# EM&bull;Bytes &ndash; Benchmark[et]ing ultra-low-power


<!-- --8<-- [start:excerpt] -->

<div class="article-meta" markdown>:calendar: October 1, 2025&thinsp; · :stopwatch: 7 min read</div>

Vendor data sheets might specify that an ultra-low-power MCU draws (say) **700&thinsp;nA @ 3&thinsp;V** when in its "deep-sleep" mode.  Very nice – but until we factor in our application workload, we have no way to truly assess the impact of these MCU specs on overall energy efficiency.
<!-- --8<-- [end:excerpt] -->

## From power (&thinsp;**W**&thinsp;) to energy (&thinsp;**J**&thinsp;)

Unless our MCU stays completely inert &ndash; awaiting reset in "shutdown" mode &ndash; embedded application software has undue influence upon system power consumption over time.

Consider a typical "ultra-low-power" wireless sensor tag &ndash; a class of embedded MCU applications which embody a relatively straightforward cyclic design pattern:

:one: &emsp;wakeup from deep-sleep mode<br>
:two: &emsp;acquire data from the environment<br>
:three: &emsp;analyze this data using an algorithm<br>
:four: &emsp;transmit results (wirelessly) to a gateway<br>
:five: &emsp;re-enter (low-power) deep-sleep mode

With application requirements dictating active duty-cycles ranging from once-per-second down to once-per-day, minimizing elapsed time between steps :one: through :five: would surely lower total power consumption &ndash; by re-entering "deep-sleep" that much sooner.

In practice, steps :two: and :four: involve MCU peripherals performing I/O operations at application-defined data-rates &ndash; an ADC sampling at 15&thinsp;kHz, a radio transmitting at 1&thinsp;Mbps, etc.&thinsp;  With little to do while awaiting I/O completion, software often idles within a "lite-sleep" mode.

!!! abstract "Typical MCU power specs"
    MCU **lite-sleep** mode typically consumes under **1&thinsp;mW** of power and enables interrupt response times of less than **1&thinsp;&mu;s**&thinsp;.&nbsp;  But while the CPU idles, other peripherals such as the radio could remain active &ndash; in fact drawing _more_&thinsp; power than the CPU would alone.

    By constract, MCU **deep-sleep** mode might consume well under **10&thinsp;&mu;W** of power &ndash; but wakeup times could stretch to **100s of &mu;s**&thinsp;.&thinsp;  While any active peripheral can awaken the CPU when idling, "deep-sleep" mode only powers a limited set of MCU elements (GPIOs, RTCs) which can trigger wakeup interrupts.

    Finally, MCU **active** mode &ndash; when the CPU fetches and executes instructions &ndash; will typically draw power at levels expressed as **&mu;W&thinsp;/&thinsp;Mhz**&thinsp;.&nbsp;  Standard industry metrics like **EEMBC CoreMark&reg;**&thinsp; help normalize performance claims by individual MCU vendors.

Once the MCU returns to its "active" mode &ndash; and the application finally does some useful work &ndash; the impact of software on total power consumption boils down to the _number_&thinsp; of instructions the CPU must fetch and execute.&nbsp; But how can we best quantify this impact&thinsp;???

!!! bulb "**Joules**, not **Watts**"
    As software practitioners, we need focus on total power consumption over a period of time.&thinsp; Only then can we begin to appreciate the oversized :wink: impact our code can have on overall energy efficiency.

## Profiling energy with **EM&bull;Scope**

## Quantifying energy efficiency

## Learning more about **EM&bull;Scope**
