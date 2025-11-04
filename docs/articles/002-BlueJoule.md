# The BlueJoule&trade; benchmark &mdash; EM&bull;Scope in action

<!-- --8<-- [start:excerpt] -->

<div class="article-meta" markdown>:calendar: October 29, 2025&thinsp; · :stopwatch: 6 min read</div>

A basic **Bluetooth Low Energy** beacon &ndash; continually advertising the same packet on multiple channels &ndash; serves as the "Hello World" of **BLE** applications.&thinsp; So let's see what we might learn by using **EM&bull;Scope** to measure and compare a representative set of **BLE** HW/SW platforms.

<!-- --8<-- [end:excerpt] -->

## Why we need a benchmark

**Bluetooth Low Energy** has emerged as pervavsive technology, following its initial availability on the **iPhone 4S** in October 2011.&thinsp; With a multitude of SW stacks now running on dozens of HW platforms, we find the absence of even the most basic BLE benchmark quite telling.

Promising _"5-10 years of operation on coin-cell batteries"_, a BLE beacon which adverties a small data packet once-per-second should certainly run for half a decade &ndash; or will it&thinsp;??

:arrow_right:&emsp;**MCU vendor data sheet**&thinsp;:&thinsp; 3.0&thinsp;V supply &thinsp;&rarr;&thinsp; 5&thinsp;mA TX current @&thinsp;0&thinsp;dB · 1&thinsp;&mu;A sleep current<br>
:arrow_right:&emsp;**Bluetooth 4.0 spec**&thinsp;:&thinsp; 1&thinsp;Mbps data rate · 37 byte packet size · 3 advertising channels<br>
:arrow_right:&emsp;**Average current consumption**&thinsp;:&thinsp;  &thinsp;&approx; (&thinsp;0.005<sub><i>radio</i></sub>&nbsp; + &thinsp;0.001<sub><i>sleep</i></sub>&thinsp;) mA<br>
:arrow_right:&emsp;**CR2032 coin-cell lifetime**&thinsp;:&thinsp; 225&thinsp;mAh ÷ 0.006&thinsp;mA = 37,500&thinsp;h &approx; 4.3&thinsp;years

Well, we almost made it to five years &ndash; but in reality, this system would likely run for only half that time.&thinsp; Why &ndash; because our paper model hasn't accounted for the _extra_&thinsp; power consumed when awakening the MCU from deep-sleep as well as executing the BLE stack code itself.

!!! eighth "On a personal note"
    I co-founded a BLE software and system design house in early 2011, working closely with Texas Instruments and others as well as stack vendors supporting these platforms.
    
    Lacking funds for a $10,000 power analyzer, we instead relied upon our multimeter and oscilloscope to give us (crude) visibility into HW/SW power consumption over time.

    Today, however, we can purchase a laboratory-grade power analyzer from  [JouleScope](https://www.joulescope.com/products/js220-joulescope-precision-energy-analyzer) for 10× less the cost as well an entry-level analyzer from [Nordic](https://www.nordicsemi.com/Products/Development-hardware/Power-Profiler-Kit-2) for 100× less the cost.

With power analyzers now available for any budget, let's use their capabilities to explicitly measure the overall energy consumption of a basic BLE beacon &ndash; gaining a system-level perspective on the interaction of the underlying HW/SW elements over time.

!!! bulb "But wait there's more...."
    By having different BLE HW/SW platforms implement the _same_ benchmark application, we can quantitatively score their "low-energy" claims and then rank their overall efficiency.

    A true "apples-to-apples" comparision &ndash; or should we say "blueberries-to-blueberries".&thinsp; :wink:


## Bringing **EM&bull;Scope** to bear

We've introduced **EM&bull;Scope** in an earlier [article](../articles/001-Benchmark.md) &ndash; and already previewed some results found in the [em-foundation/BlueJoule](https://github.com/em-foundation/BlueJoule) repository housed on **GitHub**.&thinsp; Time now for a deeper-dive.

Consistent with the **EM&bull;Scope** methodology, the **BlueJoule** benchmark requires the platform-under-test to advertise 19-bytes of payload on all three BLE advertising channels once-per-second.&thinsp; Refer to this section of the **BlueJoule** [ReadMore](https://github.com/em-foundation/BlueJoule/blob/main/docs/ReadMore.md#application) for more details.

We continue to benchmark a growing catalog of popular BLE devices:

|  |  |
|:-|:-|
|Analog Devices MAX32655[](https://www.analog.com/en/products/max32655.html)|100 MHz ARM Cortex-M4 &thinsp;&#8226;&thinsp; 512 KB flash &thinsp;&#8226;&thinsp; 128 KB SRAM|
|EM Microelectronic EM9305[](https://www.emmicroelectronic.com/product/standard-protocols/em-bleu-em9305)|48 MHz ARC EM7D &thinsp;&#8226;&thinsp; 512 KB flash &thinsp;&#8226;&thinsp; 64 KB SRAM|
|InPlay IN100[](https://inplay-tech.com/in100)|BLE beacon ASIC &thinsp;&#8226;&thinsp; no-code configuration|
|Nordic nRF52832[](https://www.nordicsemi.com/Products/nRF52832)|64 MHz ARM Cortex-M4 &thinsp;&#8226;&thinsp; 512 KB flash &thinsp;&#8226;&thinsp; 64 KB SRAM|
|Nordic nRF54L15[](https://www.nordicsemi.com/Products/nRF54L15)|128 MHz ARM Cortex-M33 &thinsp;&#8226;&thinsp; 1.5 MB flash &thinsp;&#8226;&thinsp; 256 KB SRAM|
|Silicon Labs EFR32xG22E[](https://www.silabs.com/wireless/bluetooth/efr32bg22-series-2-socs)|76.8 MHz ARM Cortex-M33 &thinsp;&#8226;&thinsp; 512 KB flash &thinsp;&#8226;&thinsp; 32 KB SRAM|
|Texas Instruments CC2340R5[](https://www.ti.com/product/CC2340R5)|48 MHz ARM Cortex-M0+ &thinsp;&#8226;&thinsp; 512 KB flash &thinsp;&#8226;&thinsp; 64 KB SRAM|

Using a **JS220** or **PPK2** analyzer, we powered each HW/SW configuration at an "optimal" input voltage when capturing data using **EM&bull;Scope**.&thinsp; We've also recorded captures for most configurations at a "standard" voltage &thinsp;&ge;&thinsp; 3V0.

<a name="voltages"></a>
!!! abstract "Input voltages"
    The BLE devices in our catalog invariably target systems powered by batteries or harvested energy.&thinsp; Arguably, we should benchmark each configuration at 3V0 and 1V5 &ndash; reflecting the nominal voltage sourced by standard batteries.

    Some BLE devices already integrate a DC/DC converter to buck&thinsp;·&thinsp;boost the source voltage to an appropriate internal level.&thinsp; In other situations, the device may require an external _power-management_&thinsp; IC to handle a 3V0 or 1V5 input source.

    This approach further reinforces our belief that improving energy efficiency within resource-constrained embedded systems requires a holistic perspective.&thinsp; All the more power &ndash; or "all the less energy" &ndash; to those devices which can operate directly from a 1V5 input voltage.

In a number of instances, we've also benchmarked the _same_&thinsp; hardware platform executing _different_&thinsp; software stacks &ndash; with some notable differences, as we'll highlight later.

You'll find the latest set of benchmark scores in this section of the **BlueJoule** [ReadMore](https://github.com/em-foundation/BlueJoule/blob/main/docs/ReadMore.md#scores).


## Mining the **EM&bull;eralds**

Lots of numbers here &nbsp;:exploding_head:&nbsp; so let's break down the results:&nbsp;  An earlier [article](../articles/001-Benchmark.md#quantifying-energy-efficiency)  introduced the **EM&bull;erald** as a measure of energy efficiency.&thinsp; Suffice it to say, one **EM&bull;erald** approximates one month of execution on a CR2032 coin-cell battery &ndash; higher score, greater efficiency.

We'll now focus on a handful of [JS220 Capture](https://github.com/em-foundation/BlueJoule/blob/main/docs/ReadMore.md#js220-scores) scores, recorded at 3V0 using our high-precision **JouleScope** analyzer (sampling at 2&thinsp;MHz).(1) While not necessarily their best scores, these 3V0 captures allow us to check our measurements against vendor datasheets.
{ .annotate }

1. You'll also find [PPK2 Capture](https://github.com/em-foundation/BlueJoule/blob/main/docs/ReadMore.md#ppk2-scores) scores, recorded at 100&thinsp;kHz using the **Nordic** analyzer.


 Let's begin with the **Texas Instruments CC2340R5&thinsp;·&thinsp;SimpleLink SDK&thinsp;·&thinsp;3V0** configuration &ndash; labeled `ti-23-lp/simplelink-3V0` and scoring 28.74 **EM&bull;eralds** for the 1&thinsp;s event period.&thinsp; A file named [`ABOUT.md`](https://github.com/biosbob/BlueJoule/blob/main/captures/js220/ti-23-lp/simplelink-3V0/ABOUT.md) delivered with each capture contains the next level of benchmark results.

!!! Hint "Tip"
    Links within the [BlueJoule](https://github.com/em-foundation/BlueJoule/blob/main/docs/ReadMore.md#catalog)&thinsp; **Catalog** and **Capture** tables will take you inside the corresponding `About.md` file for a particular HW/SW configuration.

In addition to more detailed power metrics for active execution as well as "deep-sleep", each [`ABOUT.md`](https://github.com/biosbob/BlueJoule/blob/main/captures/js220/ti-23-lp/simplelink-3V0/ABOUT.md)&thinsp; file features a screenshot depicting power consumption over time within a typical BLE advertising event.

So let's now compare the **Texas Instruments** results with scores captured on com&shy;petitive devices from **Nordic** [`nrf-54-dk/zephyr-3V0`](https://github.com/biosbob/BlueJoule/blob/main/captures/js220/nrf-54-dk/zephyr-3V0/ABOUT.md)&thinsp; and **Silicon Labs** [`sil-g22-ehk/rail-3V0`](https://github.com/biosbob/BlueJoule/blob/main/captures/js220/sil-g22-ehk/rail-3V0/ABOUT.md) :

<figure markdown id="fig1">
<img src="/assets/fig-002-1.png" width="900">
<figcaption>Texas Instruments CC2340R5 · SimpleLink SDK · 3V0
</figure>

<figure markdown id="fig2">
<img src="/assets/fig-002-2.png" width="900">
<figcaption>Nordic nRF54L15 · Zephyr OS · 3V0
</figure>

<figure markdown id="fig1">
<img src="/assets/fig-002-3.png" width="900">
<figcaption>SiLabs EFR32xG22E · Simplicity (RAIL) · 3V0
</figure>

Right away, we see differences in power consumption when actively transmitting the same 19-bytes packet on all three BLE advertising channels.&thinsp; At almost 17&thinsp;mW, this leaves **Texas Instruments** at a slight disadvantage against **Nordic** [&approx; 15&thinsp;mW] and **Silicon Labs** [&approx; 16&thinsp;mW].

But standing back and looking at the advertising event as a whole, other factors can contribute to the _total_&thinsp; amount of power consumed over this period of time:

:blue_square: &ensp; the time for the HW to transition from "sleep" to "active" mode<br>
:blue_square: &ensp; the time waiting for a high-frequency radio crystal to stabilize<br>
:blue_square: &ensp; the time initializing the BLE stack and preparing the radio<br>
:blue_square: &ensp; the time in transition between one packet and the next<br>
:blue_square: &ensp; the time to shutdown the stack and re-enter "sleep"

Each of the HW/SW platforms benchmarked here has its own strengths and weaknesses in these areas.&thinsp; And since packet transmission often accounts for &lt;&thinsp;50% of the total power consumed when active, this "overhead" requires further sruntity in our hunt for more **EM&bull;eralds**.

Last but not least, let's understand the impact of average sleep current on overall energy efficiency.&thinsp; The notable gap between **Texas Instruments** [0.5&thinsp;&mu;A] and **Nordic** [2.8&thinsp;&mu;A] will clearly help the former and hurt the latter in this sort of benchmark.

Sleep current in fact dominates as we _increase_&thinsp; our event period from one-second to ten-seconds.&thinsp; After measuring sleep current as well as energy consumption of a typical event, **EM&bull;Scope** can extrapolate **EM&bull;erald** scores for _any_&thinsp; period of interest to our application.

!!! eighth "On a personal note"
    In some configurations, I've replaced the BLE stack supplied by the silicon vendor with one of my own design written in [EM&bull;Script](https://docs.emscript.openem.org) &ndash; a novel programming platform which targets resource-constrained MCUs.

    By optimizing both code size and execution time, we can potentially _improve_&thinsp; overall energy efficiency.&thinsp; **EM&bull;erald** scores of 52.91 and 316.70 turned in by the [`ti-23-lp/emscript-2V2`](https://github.com/em-foundation/BlueJoule/blob/main/captures/ppk2/ti-23-lp/emscript-2V2/ABOUT.md) capture should peak your interest &ndash; and will receive more attention in future articles.

## Helping the cause

If nothing else, **BlueJoule** fills a void in the industry &ndash; not only by streamlining comparision of one "ultra-low-power" BLE device against another, but also by giving us greater insight into _how_&thinsp; these devices consume energy when executing an application workload in real-time.

To engage at the next level, the **EM&bull;Scope** [ReadMore](https://github.com/em-foundation/emscope/blob/docs-stable/docs/ReadMore.md#installation) shows you how to install and use this open-source tool &ndash; drawing on our `ti-23-lp/simplelink-3V0` capture as a working example.

!!! bulb "... and you don't need a power analyzer to start exploring the benchmark results !!!"

The **BlueJoule** [ReadMore](https://github.com/em-foundation/BlueJoule/blob/main/docs/ReadMore.md#contributing) provides additional information for anyone wishing to submit a _new_&thinsp; capture using **EM&bull;Scope** in conjunction with a **JS220** or **PPK2** analyzer.

But above all, we need input from the BLE device vendors publicized by our efforts:

:question::question: &ensp; is **BlueJoule** a meaningful benchmark<br>
:question::question: &ensp; have we measured your device fairly<br>
:question::question: &ensp; are there other devices of interest<br>
:question::question: &ensp; how do we best interact with you

Ideally, each vendor would deliver optimized `bluejoule` SDK projects targeting specific BLE devices within their silicon portfolio &ndash; not unlike the ever-present `coremark` projects we find.

!!! eighth "On a personal note"
    Having prepared most of the software used in the current **BlueJoule** catalog, I can honestly attest to the relative difficultly of this task &ndash; given that an energy-efficient periodic advertising example should seemingly serve as the "hello world" of BLE.

    I often found myself dissecting sophisticated, generalized applications to finally arrive at an elementary embodiment of the BLE broadcast role.&thinsp; More important, I sometimes had to _add_&thinsp; instructions to ensure the application  enters the lowest-power sleep mode.

    As a multi-decade veteren of this industry, I understand the challenges silicon vendors can face &ndash; and would therefore offer to work with y'all in making **BlueJoule** a reality.

{[hc]}
