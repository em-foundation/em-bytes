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

    Today, however, we can purchase a laboratory-grade power analyzer from [JouleScope](https://www.joulescope.com/products/js220-joulescope-precision-energy-analyzer) for 10× less the cost as well an entry-level analyzer from [Nordic](https://www.nordicsemi.com/Products/Development-hardware/Power-Profiler-Kit-2) for 100× less the cost.

With power analyzers now available for any budget, let's use their capabilities to explicitly measure the overall energy consumption of a basic BLE beacon &ndash; gaining a system-level perspective on the interaction of the underlying HW/SW elements over time.

!!! bulb "But wait there's more...."
    By having different BLE HW/SW platforms implement the _same_ benchmark application, we can quantitatively score their "low-energy" claims and then rank their overall efficiency.

    A true "apples-to-apples" comparision &ndash; or should we say "blueberries-to-blueberries".&thinsp; :wink:


## Bringing **EM&bull;Scope** to bear

## What do these scores mean

## Contributing to the cause