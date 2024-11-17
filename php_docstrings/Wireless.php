<?php
/**
 * Wireless RRD Type
 * -----------------
 * 
 * This class represents a Wireless RRD type, extending the Base class.
 * It defines the heartbeat, minimum, and maximum values for the datasets.
 * 
 * *Params*
 * 
 *  - argsv[0] : str
 *     - The filename of the RRD file.
 * 
 * *Arguments* 
 *   -   None
 *
 * *Datasets*
 * 
 *   -   snr : GAUGE
 *     - Signal-to-Noise Ratio dataset.
 *   -   rate : GAUGE
 *     - Data rate dataset.
 *   -   channel : GAUGE
 *     - Channel dataset.
 */