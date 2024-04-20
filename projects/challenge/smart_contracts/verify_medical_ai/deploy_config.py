import logging

import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient
from algosdk import account

logger = logging.getLogger(__name__)


def can_i_trust_this_ai(
    ai_info,
) -> bool:
    if (
        ai_info.mcat_score < 510
        or ai_info.residency_training is False
        or ai_info.medical_license is False
    ):
        return False
    return True


# define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.verify_medical_ai.client import (
        VerifyMedicalAiClient,
    )

    app_client = VerifyMedicalAiClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client,
    )

    app_client.app_client.create()
    logger.info(f"Deployed contract with app_id {app_client.app_id}")

    app_client.compose().opt_in_bare().record_ai_info(
        name="GPT-7-Doctor",
        used_model="Convolutional Neural Networks (CNNs)",
        medical_degree="Doctor of Medicine from Harvard Medical School",
        mcat_score=510,
        residency_training=True,
        medical_license=True,
    ).execute()

    response = app_client.get_ai_info().return_value
    logger.info(f"Medical AI name: {response.name}")
    logger.info(f"Medical AI model: {response.used_model}")
    logger.info(f"Medical AI Degree: {response.medical_degree}")

    ai_is_valid = can_i_trust_this_ai(response)
    logger.info(f"Can I trust this AI? {ai_is_valid}")

    ### Record another Medical AI that is not trustworthy
    sk, addr = account.generate_account()
    account2 = algokit_utils.Account(private_key=sk, address=addr)

    algokit_utils.ensure_funded(
        algod_client,
        algokit_utils.EnsureBalanceParameters(
            account_to_fund=account2, min_spending_balance_micro_algos=10000000
        ),
    )
    VerifyMedicalAiClient(
        algod_client,
        indexer_client=indexer_client,
    )

    app_client2 = VerifyMedicalAiClient(
        algod_client,
        app_id=app_client.app_id,
        signer=account2,
        sender=account2.address,
    )

    app_client2.compose().opt_in_bare().record_ai_info(
        name="GPT-2-Doctor",
        used_model="Convolutional Neural Networks (CNNs)",
        medical_degree="Doctor of Medicine from Harvard Medical School",
        mcat_score=370,
        residency_training=False,
        medical_license=False,
    ).execute()

    response = app_client2.get_ai_info().return_value
    logger.info(f"Medical AI name: {response.name}")
    logger.info(f"Medical residency training completed?: {response.residency_training}")
    logger.info(f"Medical license?: {response.medical_license}")

    ai_is_valid = can_i_trust_this_ai(response)
    logger.info(f"Can I trust this AI? {ai_is_valid}")
