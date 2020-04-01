from easyvvuq.decoders.json import JSONDecoder
import os
import numpy as np


def test_jsondecoder_basic():
    decoder = JSONDecoder(os.path.join('jsondecoder', 'fredrik.json'), ['cfrac', 'we', 'v'])
    run_info = {'run_dir': 'tests'}
    data = decoder.parse_sim_output(run_info)
    assert((data['cfrac'] == np.array([0.24000000131541285])).all().all())
    assert((data['we'] == np.array([-0.4910355508327484])).all().all())
    assert((data['v'] == np.array([0.014841768890619278,
                                   0.014779693447053432,
                                   0.014733896590769291,
                                   0.014711864292621613,
                                   0.01470966450870037,
                                   0.014723854139447212,
                                   0.01474687922745943,
                                   0.014768443070352077,
                                   0.01478823646903038,
                                   0.01481111440807581,
                                   0.014824368990957737,
                                   0.014829156920313835,
                                   0.014819246716797352,
                                   0.014791729860007763,
                                   0.014738374389708042,
                                   0.014660114422440529,
                                   0.014429694972932339,
                                   0.01425190269947052,
                                   0.014102380722761154,
                                   0.013794410973787308,
                                   0.013637131080031395,
                                   0.013455528765916824,
                                   0.013191652484238148,
                                   0.013099015690386295,
                                   0.012983563356101513,
                                   0.012864833697676659,
                                   0.01277084369212389,
                                   0.012721200473606586,
                                   0.012596715241670609,
                                   0.012423157691955566,
                                   0.012156027369201183,
                                   0.011878175660967827,
                                   0.01177501305937767,
                                   0.011609729379415512,
                                   0.011352979578077793,
                                   0.011070813983678818,
                                   0.010821142233908176,
                                   0.010543721728026867,
                                   0.010277168825268745,
                                   0.010026565752923489,
                                   0.009804881177842617,
                                   0.009599489159882069,
                                   0.009395209141075611,
                                   0.00917865987867117,
                                   0.008997873403131962,
                                   0.008819280192255974,
                                   0.008683303371071815,
                                   0.008515624329447746,
                                   0.00831963773816824,
                                   0.008140306919813156,
                                   0.007954764179885387,
                                   0.007770225405693054,
                                   0.00758766196668148,
                                   0.007404009811580181,
                                   0.00722180400043726,
                                   0.007042537909001112,
                                   0.006860550958663225,
                                   0.006680922582745552,
                                   0.006502178963273764,
                                   0.006320721469819546,
                                   0.00613985862582922,
                                   0.00595864886417985,
                                   0.0057795993052423,
                                   0.005598034244030714,
                                   0.005417921114712954,
                                   0.005241408012807369,
                                   0.005052104126662016,
                                   0.004876876249909401,
                                   0.004697349388152361,
                                   0.004517038818448782,
                                   0.004333806689828634,
                                   0.00415557436645031,
                                   0.003969619516283274,
                                   0.003797980025410652,
                                   0.003611199092119932,
                                   0.0034324300941079855,
                                   0.0032506941352039576,
                                   0.0030704534146934748,
                                   0.002888839691877365,
                                   0.002707288833335042,
                                   0.0025427646469324827,
                                   0.002415195805951953,
                                   0.002359578385949135,
                                   0.0023344780784100294,
                                   0.0023027241695672274,
                                   0.002270693425089121,
                                   0.0022391551174223423,
                                   0.0022060663904994726,
                                   0.00217291503213346,
                                   0.0021398148965090513,
                                   0.00210800813511014,
                                   0.002074991352856159,
                                   0.002041975734755397,
                                   0.0020094725769013166,
                                   0.0019798376597464085,
                                   0.0019466927042230964,
                                   0.0019146542763337493,
                                   0.0018817033851519227,
                                   0.0018483188468962908,
                                   0.0018153132405132055,
                                   0.0017822484951466322,
                                   0.0017517984379082918,
                                   0.0017170008504763246,
                                   0.00168553926050663,
                                   0.0016540634678676724,
                                   0.0016217215452343225,
                                   0.0015883957967162132,
                                   0.0015583134954795241,
                                   0.0015226758550852537,
                                   0.001490586786530912,
                                   0.0014588346239179373,
                                   0.0014263952616602182,
                                   0.001393234240822494,
                                   0.0013616280630230904,
                                   0.0013303045416250825,
                                   0.0012980689061805606,
                                   0.0012646319810301065,
                                   0.0012320373207330704,
                                   0.0011981468414887786,
                                   0.0011661312310025096,
                                   0.0011351823341101408,
                                   0.0011039526434615254,
                                   0.00107281981036067,
                                   0.0010381652973592281,
                                   0.0010054642334580421,
                                   0.0009733123588375747])).all().all())


def test_jsondecoder_scalars_only():
    # like test_jsondecoder_basics, but with only scalar quantities
    decoder = JSONDecoder(os.path.join('jsondecoder', 'fredrik.json'), ['cfrac', 'we'])
    run_info = {'run_dir': 'tests'}
    data = decoder.parse_sim_output(run_info)
    assert((data['cfrac'] == np.array([0.24000000131541285])).all().all())
    assert((data['we'] == np.array([-0.4910355508327484])).all().all())


def test_json_nested():
    decoder = JSONDecoder(os.path.join('jsondecoder', 'nested.json'),
                          [['root1', 'node1', 'leaf1'], ['root1', 'leaf2'], 'leaf3'])
    run_info = {'run_dir': 'tests'}
    data = decoder.parse_sim_output(run_info)
    assert((data['root1.node1.leaf1'] == np.array([0.33])).all().all())
    assert((data['root1.leaf2'] == np.array([0.32])).all().all())
    assert((data['leaf3'] == np.array([0.2, 0.3])).all().all())


def test_get_restart_dict():
    decoder = JSONDecoder('nested.json',
                          [['root1', 'node1', 'leaf1'], ['root1', 'leaf2'], 'leaf3'])
    restart_dict = decoder.get_restart_dict()
    assert(restart_dict['target_filename'] == 'nested.json')
    assert(restart_dict['output_columns'] ==
           [['root1', 'node1', 'leaf1'], ['root1', 'leaf2'], 'leaf3'])
