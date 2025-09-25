# EM&bull;Bytes &thinsp;**&#183;**&thinsp; Quantifying energy efficiency with EM&bull;Scope


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
    As software practitioners, we need focus on total power consumption over a period of time.&thinsp; Only then can we begin to appreciate the oversized :wink: impact our code might have on overall energy efficiency.

## Profiling energy with **EM&bull;Scope**

To bring energy efficiency into the foreground, we've introduced **EM&bull;Scope** &ndash; a tool used to capture, analyze, display, and deliver real-time profiles of power-consumption.

Measuring target embedded systems performing typical periodic functions, **EM&bull;Scope** offers insights to developers and integrators alike not found in the MCU data sheet &ndash; by adding the dimension of _time_&thinsp; to the equation.

!!! eighth "On a personal note"
    Back in the day, I never really worried about _minimizing_&thinsp; system power consumption when developing embedded application software.&thinsp; Instead, we fixated on _maximizing_&thinsp; processor utilization &ndash; using every available MIP to continuously perform a multitude of real-time tasks.

    In my mind, the **Texas Instruments MSP430** (announced in the 1990s) set the performance standard for the _ultra-low-power_&thinsp; microcontroller as we know it today.&thinsp; If nothing else, the MSP430 stands alone as the first MCU to use items from your [fridge](https://www.youtube.com/watch?v=nPZISRQAQpw) as a power source.

    As a software developer, the rules of the game have now changed &ndash; to one in which "doing nothing" for the longest possible time _maximizes_ overall energy efficiency.&thinsp; Yes, we still want to execute code as quickly as possible &ndash; so we can enjoy a "deep-sleep" that much sooner.

**EM&bull;Scope** captures real-time information via a hardware _power analyzer_&thinsp; connected to your target MCU board as well as your host PC:

<figure markdown id="fig1">
![Image info](/assets/fig-001-1.png)
<figcaption>EM&bull;Scope Configuration 
</figure>


## Quantifying energy efficiency

## Learning more about **EM&bull;Scope**
