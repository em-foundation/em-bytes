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

In a number of instances, we've benchmarked the _same_&thinsp; hardware platform executing _different_&thinsp; software stacks &ndash; with notable differences in several cases.

Using a **JS220** or **PPK2** analyzer, we powered each HW/SW configuration at 3V3 when capturing data using **EM&bull;Scope**.&thinsp; Where appropriate, we also recorded the benchmark at a more "optimal" input voltage (such as 1V8).

<a name="voltages"></a>
!!! abstract "Standard input voltages"
    The BLE devices in our catalog invariably target systems powered by batteries or harvested energy.&thinsp; Arguably, we should benchmark each configuration at 3V0 and 1V5 &ndash; reflecting the nominal voltage sourced by standard batteries.

    Some BLE devices already integrate a DC/DC converter to buck-boost the source voltage to an appropriate internal level.&thinsp; In other situations, the device may require an external _power-management_&thinsp; IC to handle a 3V0 or 1V5 input source.

    This approach further reinforces our belief that improving the overall energy efficiency of resource-constrained embedded systems requires a holistic perspective.

You'll find the latest set of benchmark scores in this section of the **BlueJoule** [ReadMore](https://github.com/em-foundation/BlueJoule/blob/main/docs/ReadMore.md#scores).


## Mining the **EM&bull;eralds**

Lots of numbers here &nbsp;:exploding_head:&nbsp; so let's break down the results:&nbsp;  An earlier [article](../articles/001-Benchmark.md#quantifying-energy-efficiency)  introduced the **EM&bull;erald** as a measure of energy efficiency.&thinsp; Suffice it to say, one EM&bull;erald approximates one month of execution on a CR2032 coin-cell battery &ndash; higher score, greater efficiency.

We'll explore a set of [JS220 Capture](https://github.com/em-foundation/BlueJoule/blob/main/docs/ReadMore.md#js220-scores) scores, recorded with our high-precision **JouleScope** analyzer which samples input signals at 2&thinsp;MHz.(1) Let's begin by comparing scores for a one-second event period powered at 3.3&thinsp;Volts, found in the column labeled&thinsp; **00:00:01&nbsp;·&nbsp;3V3**.
{ .annotate }

1. We've also published a set of [PPK2 Capture](https://github.com/em-foundation/BlueJoule/blob/main/docs/ReadMore.md#ppk2-scores) scores, recorded at 100&thinsp;kHz using the **Nordic** analyzer.

As a starting point, let's drill-down on the **Texas Instruments CC2340R5&thinsp;·&thinsp;SimpleLink SDK** configuration [`ti-23-lp/simplelink`] &ndash; scoring a respectible 28.13 EM&bull;eralds.&thinsp; A file named [`ABOUT.md`](https://github.com/biosbob/BlueJoule/blob/main/captures/js220/ti-23-lp/simplelink/ABOUT.md)&thinsp; (delivered with each capture) contains the next level of benchmark results.

!!! Hint "Tip"
    Links within the [BlueJoule](https://github.com/em-foundation/BlueJoule/blob/main/docs/ReadMore.md#catalog)&thinsp; **Catalog** and **Capture** tables will take you inside the corresponding `About.md` file for a particular HW/SW configuration.

In addition to more detailed power metrics for active execution as well as "deep-sleep", each [`ABOUT.md`](h ttps://github.com/biosbob/BlueJoule/blob/main/captures/js220/ti-23-lp/simplelink/ABOUT.md)&thinsp;  file features a screenshot of a typical BLE advertising event.&thinsp; Our earlier [article](../articles/001-Benchmark.md#fig2) introducing the capabilities of **EM&bull;Scope** in fact presented this same picture.

Let's now compare the **Texas Instruments** results with BlueJoule scores captured on com&shy;petitive devices from **Nordic** [`nrf-54-dk/zephyr`](https://github.com/biosbob/BlueJoule/blob/main/captures/js220/nrf-54-dk/zephyr/ABOUT.md)&thinsp; and **Silicon Labs** [`sil-g22-ehk/rail`](https://github.com/biosbob/BlueJoule/blob/main/captures/js220/sil-g22-ehk/rail/ABOUT.md) :

<figure markdown id="fig1">
![Image info](/assets/fig-002-1.png)
<figcaption>Texas Instruments CC2340R5 · SimpleLink SDK · 3V3
</figure>

<figure markdown id="fig2">
![Image info](/assets/fig-002-2.png)
<figcaption>Nordic nRF54L15 · Zephyr OS · 3V3
</figure>

<figure markdown id="fig1">
![Image info](/assets/fig-002-3.png)
<figcaption>SiLabs EFR32xG22E · Simplicity (RAIL) · 3V3
</figure>

Right away, we see differences in power consumption when actively transmitting the same 19-bytes packet on all three BLE advertising channels.&thinsp; At almost 18&thinsp;mW, this puts **Texas Instruments** at a slight disadvantage against **Nordic** [&approx; 15&thinsp;mW] and **Silicon Labs** [&approx; 16&thinsp;mW].

But standing back and looking at the advertising event as a whole, other factors can contribute to the total amount of power consumed over this period of time:

:blue_square: &ensp; the time for the HW to transition from "sleep" to "active" mode<br>
:blue_square: &ensp; the time waiting for a high-frequency radio crystal to stabilize<br>
:blue_square: &ensp; the time initializing the BLE stack and preparing the radio<br>
:blue_square: &ensp; the time in transition between one packet and the next<br>
:blue_square: &ensp; the time to shutdown the stack and re-enter "sleep"

Each of the HW/SW platforms benchmarked here has its own strengths and weaknesses in these areas.&thinsp; And since packet transmission often accounts for &lt;&thinsp;50% of the total power consumed when active, this "overhead" requires further sruntity in our hunt for more **EM&bull;eralds**.

Last but not least, let's understand the impact of average sleep current on overall energy efficiency.&thinsp; The notable gap between **Texas Instruments** [0.417&thinsp;&mu;A] and **Nordic** [3.505&thinsp;&mu;A] will clearly help the former and hurt the latter in this sort of benchmark.

Sleep current in fact dominates as we _increase_&thinsp; our event period from one-second to ten-seconds.&thinsp; After measuring sleep current as well as energy consumption of a typical event, **EM&bull;Scope** can extrapolate **EM&bull;erald** scores for _any_&thinsp; period of interest to our application.

We've talked [earlier](#voltages) about standardizing input voltage(s) used in these captures.&thinsp; Needless to say, a very different set of scores emerge when powering the underlying hardware at lower voltages ranging from 2V2 down to 1V5 &ndash; as seen in the column labeled [00:00:01&nbsp;·&nbsp;<i>d</i>&thinsp;V<i>d</i>&thinsp;](https://github.com/em-foundation/BlueJoule/blob/main/docs/ReadMore.md#js220-score)&thinsp;.

!!! eighth "On a personal note"
    In some configurations, I've replaced the BLE stack supplied by the silicon with one of my own design writing in [EM&bull;Script]("https://docs.emscript.openem.org) &ndash; a novel programming platform which targets resource-constrained MCUs.

    By optimizing both code size and execution time, we can potentially _improve_&thinsp; overall energy efficiency.&thinsp; The **EM&bull;erald** scores of 38.29 and 214.10 recorded within the [`ti-23-lp/emscript`](https://github.com/em-foundation/BlueJoule/blob/main/captures/ppk2/ti-23-lp/emscript/ABOUT.md) capture should peak your interest &ndash; and will receive more attention in future articles.





## Contributing to the cause