import sys
import os
import unittest

# Setup paths
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'brain-py'))

from core.militar_v1 import BaseMilitar as BaseMilitarV1, SistemaEconomico
from core.militar_v2 import BaseMilitar as BaseMilitarV2
from security_kernel import SentinelKernel, SecurityGuardian

class TestIsolation(unittest.TestCase):
    def test_class_isolation(self):
        # BaseMilitarV1 doesn't need economy
        base1 = BaseMilitarV1("North", "Alpha")
        # BaseMilitarV2 needs economy
        econ = SistemaEconomico(1000, 100)
        base2 = BaseMilitarV2("South", "Beta", econ)

        # Check they are different classes with different signatures
        self.assertNotEqual(type(base1), type(base2))
        print("✅ Isolamento de Classe: OK")

    def test_falha_45_mitigation(self):
        sentinel = SentinelKernel()
        # Simulate instability drop
        sentinel.update_stability(-145)
        self.assertEqual(sentinel.stability_level, -45)

        # Action should be blocked
        allowed = sentinel.validate_action("ECON_DRAIN", {})
        self.assertFalse(allowed)
        self.assertTrue(sentinel.cardinal_valve_active)
        print("✅ Mitigação Falha -45: OK")

    def test_security_guardian(self):
        self.assertTrue(SecurityGuardian.validate_command("CMD-123456"))
        self.assertFalse(SecurityGuardian.validate_command("INVALID"))
        print("✅ Security Guardian (CMD): OK")

if __name__ == "__main__":
    unittest.main()
