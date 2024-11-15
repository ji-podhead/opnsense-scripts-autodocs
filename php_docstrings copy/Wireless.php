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
 * - filename : str
 *     index: 1
 *     The filename of the RRD file.
 * 
 * *Arguments*
 * 
 * - None
 * 
 * *Returns*
 * 
 * - None
 * 
 * *Datasets*
 * 
 * - snr : GAUGE
 *     Signal-to-Noise Ratio dataset.
 * - rate : GAUGE
 *     Data rate dataset.
 * - channel : GAUGE
 *     Channel dataset.
 */