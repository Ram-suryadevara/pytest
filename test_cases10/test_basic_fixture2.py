# Using the fixture supply_AA_BB_CC from conftest.file. 



def test_comparewithAA_file2(data_abc):
    zz = 25
    assert data_abc[0] == zz, "aa and zz comparison failed"


def test_comparewithBB_file2(data_abc):
    zz = 35
    assert data_abc[1] == zz, "bb and zz comparison failed"


def test_comparewithCC_file2(data_abc):
    zz = 25
    assert data_abc[2] == zz, "cc and zz comparison failed"
