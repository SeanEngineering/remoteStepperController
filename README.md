# remoteStepperController

The purpose of this project is to manipulate an off the shelf LY-GRBL4-12287-V3 a series of stepper motors remotely.
This controller can be found [here](https://ja.aliexpress.com/item/1005003912562799.html?spm=a2g0o.productlist.0.0.1e1a44dcnvRoau&algo_pvid=ba56a90c-3ae0-40fc-b52f-9c15aa6d02ca&algo_exp_id=ba56a90c-3ae0-40fc-b52f-9c15aa6d02ca-12&pdp_ext_f=%7B%22sku_id%22%3A%2212000027452471764%22%7D&pdp_npi=2%40dis%21AUD%21120.43%2173.46%21%21%21%21%21%40210318cb16704489692995261e8f80%2112000027452471764%21sea&curPageLogUid=5wkP4Evp3HCh)

To get this to work the following objectives will need to be understood:

-   Identify Gcode command logic.
-   Identify how to establish a serial communication to the controller.
-   Identify how to send a command over the serial port.
-   Convert Gcode to byte information.
-   Create basic movement functions

The universal g-code controller (UGS) will be used as a reference point to understand the basics (https://github.com/winder/Universal-G-Code-Sender)

This code is written in Python.

## Gcode Command logic

How Gcode works: https://howtomechatronics.com/tutorials/g-code-explained-list-of-most-important-g-code-commands/

-   G01 X Y F50 will be used for initial testing.
