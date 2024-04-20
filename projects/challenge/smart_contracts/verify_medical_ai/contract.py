from algopy import ARC4Contract, arc4, LocalState, Txn, UInt64, Global, op


class AiInfo(arc4.Struct):
    name: arc4.String
    used_model: arc4.String
    medical_degree: arc4.String
    mcat_score: arc4.UInt64
    residency_training: arc4.Bool
    medical_license: arc4.Bool


class VerifyMedicalAI(ARC4Contract):
    def __init__(self) -> None:
        self.ai_info = LocalState(AiInfo)

    @arc4.baremethod(allow_actions=["OptIn"])
    def opt_in(self) -> None:
        self.ai_info[Txn.sender] = AiInfo(
            name=arc4.String(""),
            used_model=arc4.String(""),
            medical_degree=arc4.String(""),
            mcat_score=arc4.UInt64(0),
            residency_training=arc4.Bool(False),
            medical_license=arc4.Bool(False),
        )

    @arc4.abimethod()
    def record_ai_info(
        self,
        name: str,
        used_model: str,
        medical_degree: str,
        mcat_score: UInt64,
        residency_training: bool,
        medical_license: bool,
    ) -> None:
        self.ai_info[Txn.sender] = AiInfo(
            name=name,
            used_model=used_model,
            medical_degree=medical_degree,
            mcat_score=mcat_score,
            residency_training=residency_training,
            medical_license=medical_license,
        )

    @arc4.abimethod(readonly=True)
    def get_ai_info(self) -> AiInfo:
        assert op.app_opted_in(Txn.sender, Global.current_application_id)
        return self.ai_info[Txn.sender]
