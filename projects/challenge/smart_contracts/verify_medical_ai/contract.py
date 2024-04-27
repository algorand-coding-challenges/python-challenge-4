from algopy import ARC4Contract, arc4, LocalState, Txn, UInt64, Global, op, String


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
        name: String,
        used_model: String,
        medical_degree: String,
        mcat_score: UInt64,
        residency_training: bool,
        medical_license: bool,
    ) -> None:
        self.ai_info[Txn.sender] = AiInfo(
            name=arc4.String(name),
            used_model=arc4.String(used_model),
            medical_degree=arc4.String(medical_degree),
            mcat_score=arc4.UInt64(mcat_score),
            residency_training=arc4.Bool(residency_training),
            medical_license=arc4.Bool(medical_license),
        )

    @arc4.abimethod(readonly=True)
    def get_ai_info(self) -> AiInfo:
        assert op.app_opted_in(Txn.sender, Global.current_application_id)
        return self.ai_info[Txn.sender]
