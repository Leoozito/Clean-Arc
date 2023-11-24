# Casos de uso: Para criar uma estampagem, deletar estampagem, alterar estampagem.
from estampador_service.application.estampagens.estampagens_dto import EstampagensDto
from estampador_service.domain.estampagens.enums import *
from estampador_service.domain.estampagens.exceptions import *

class EstampagensManager(object):
    def iniciar_registro_estampagem(self, estampagensDto: EstampagensDto):
        estampagens_aggregate = estampagensDto.to_domain()

        try:
            if estampagens_aggregate.is_valid():
                return {'message': SuccessCodes.SUCCESS.value, 'code': SuccessCodes.SUCCESS.value}
            # estampagens_aggregate.create_booking()
            # final_dto = estampagensDto.to_dto(estampagens_aggregate)
            # self.storage.save_booking(final_dto)
            # return {'message': SuccessCodes.SUCCESS.value, 'code': SuccessCodes.SUCCESS.name}
        except RegisterDateCannotAfterConclusaoDate as e:
            return {'message': ErrorCodes.REGISTERAFTERCONCLUSAO.value, 'code': ErrorCodes.REGISTERAFTERCONCLUSAO.name}
        except PlacasCannotBeForgotten as e:
            return {'message': ErrorCodes.PLACASREQUIRED.value, 'code': ErrorCodes.PLACASREQUIRED.name}
        except EstampagemUpdateRequiredAE as e:
            return {'message': ErrorCodes.REGISTERSSHOULDBENUMBERAE.value, 'code': ErrorCodes.REGISTERSSHOULDBENUMBERAE.name}
        except EstampagemStatusCannotBeDelete as e:
            return {'message': ErrorCodes.INVALIDREGISTER.value, 'code': ErrorCodes.INVALIDREGISTER.name}
        except Exception as e:
            return {'message': ErrorCodes.UNDEFINED.value, 'code': ErrorCodes.UNDEFINED.name}