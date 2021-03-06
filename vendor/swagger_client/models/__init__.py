# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online

    OpenAPI spec version: 0.6.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .delete_characters_character_id_mail_labels_label_id_unprocessable_entity import DeleteCharactersCharacterIdMailLabelsLabelIdUnprocessableEntity
from .delete_fleets_fleet_id_members_member_id_not_found import DeleteFleetsFleetIdMembersMemberIdNotFound
from .delete_fleets_fleet_id_squads_squad_id_not_found import DeleteFleetsFleetIdSquadsSquadIdNotFound
from .delete_fleets_fleet_id_wings_wing_id_not_found import DeleteFleetsFleetIdWingsWingIdNotFound
from .forbidden import Forbidden
from .get_alliances_alliance_id_icons_not_found import GetAlliancesAllianceIdIconsNotFound
from .get_alliances_alliance_id_icons_ok import GetAlliancesAllianceIdIconsOk
from .get_alliances_alliance_id_not_found import GetAlliancesAllianceIdNotFound
from .get_alliances_alliance_id_ok import GetAlliancesAllianceIdOk
from .get_alliances_names_200_ok import GetAlliancesNames200Ok
from .get_characters_character_id_agents_research_200_ok import GetCharactersCharacterIdAgentsResearch200Ok
from .get_characters_character_id_assets_200_ok import GetCharactersCharacterIdAssets200Ok
from .get_characters_character_id_attributes_ok import GetCharactersCharacterIdAttributesOk
from .get_characters_character_id_blueprints_200_ok import GetCharactersCharacterIdBlueprints200Ok
from .get_characters_character_id_bookmarks_200_ok import GetCharactersCharacterIdBookmarks200Ok
from .get_characters_character_id_bookmarks_coordinates import GetCharactersCharacterIdBookmarksCoordinates
from .get_characters_character_id_bookmarks_folders_200_ok import GetCharactersCharacterIdBookmarksFolders200Ok
from .get_characters_character_id_bookmarks_item import GetCharactersCharacterIdBookmarksItem
from .get_characters_character_id_bookmarks_target import GetCharactersCharacterIdBookmarksTarget
from .get_characters_character_id_calendar_200_ok import GetCharactersCharacterIdCalendar200Ok
from .get_characters_character_id_calendar_event_id_attendees_200_ok import GetCharactersCharacterIdCalendarEventIdAttendees200Ok
from .get_characters_character_id_calendar_event_id_ok import GetCharactersCharacterIdCalendarEventIdOk
from .get_characters_character_id_chat_channels_200_ok import GetCharactersCharacterIdChatChannels200Ok
from .get_characters_character_id_chat_channels_allowed import GetCharactersCharacterIdChatChannelsAllowed
from .get_characters_character_id_chat_channels_blocked import GetCharactersCharacterIdChatChannelsBlocked
from .get_characters_character_id_chat_channels_muted import GetCharactersCharacterIdChatChannelsMuted
from .get_characters_character_id_chat_channels_operator import GetCharactersCharacterIdChatChannelsOperator
from .get_characters_character_id_clones_home_location import GetCharactersCharacterIdClonesHomeLocation
from .get_characters_character_id_clones_jump_clone import GetCharactersCharacterIdClonesJumpClone
from .get_characters_character_id_clones_ok import GetCharactersCharacterIdClonesOk
from .get_characters_character_id_contacts_200_ok import GetCharactersCharacterIdContacts200Ok
from .get_characters_character_id_contacts_labels_200_ok import GetCharactersCharacterIdContactsLabels200Ok
from .get_characters_character_id_contracts_200_ok import GetCharactersCharacterIdContracts200Ok
from .get_characters_character_id_contracts_contract_id_bids_200_ok import GetCharactersCharacterIdContractsContractIdBids200Ok
from .get_characters_character_id_contracts_contract_id_items_200_ok import GetCharactersCharacterIdContractsContractIdItems200Ok
from .get_characters_character_id_corporationhistory_200_ok import GetCharactersCharacterIdCorporationhistory200Ok
from .get_characters_character_id_fatigue_ok import GetCharactersCharacterIdFatigueOk
from .get_characters_character_id_fittings_200_ok import GetCharactersCharacterIdFittings200Ok
from .get_characters_character_id_fittings_item import GetCharactersCharacterIdFittingsItem
from .get_characters_character_id_fleet_not_found import GetCharactersCharacterIdFleetNotFound
from .get_characters_character_id_fleet_ok import GetCharactersCharacterIdFleetOk
from .get_characters_character_id_industry_jobs_200_ok import GetCharactersCharacterIdIndustryJobs200Ok
from .get_characters_character_id_killmails_recent_200_ok import GetCharactersCharacterIdKillmailsRecent200Ok
from .get_characters_character_id_location_ok import GetCharactersCharacterIdLocationOk
from .get_characters_character_id_loyalty_points_200_ok import GetCharactersCharacterIdLoyaltyPoints200Ok
from .get_characters_character_id_mail_200_ok import GetCharactersCharacterIdMail200Ok
from .get_characters_character_id_mail_labels_label import GetCharactersCharacterIdMailLabelsLabel
from .get_characters_character_id_mail_labels_ok import GetCharactersCharacterIdMailLabelsOk
from .get_characters_character_id_mail_lists_200_ok import GetCharactersCharacterIdMailLists200Ok
from .get_characters_character_id_mail_mail_id_not_found import GetCharactersCharacterIdMailMailIdNotFound
from .get_characters_character_id_mail_mail_id_ok import GetCharactersCharacterIdMailMailIdOk
from .get_characters_character_id_mail_mail_id_recipient import GetCharactersCharacterIdMailMailIdRecipient
from .get_characters_character_id_mail_recipient import GetCharactersCharacterIdMailRecipient
from .get_characters_character_id_medals_200_ok import GetCharactersCharacterIdMedals200Ok
from .get_characters_character_id_medals_graphic import GetCharactersCharacterIdMedalsGraphic
from .get_characters_character_id_not_found import GetCharactersCharacterIdNotFound
from .get_characters_character_id_notifications_200_ok import GetCharactersCharacterIdNotifications200Ok
from .get_characters_character_id_notifications_contacts_200_ok import GetCharactersCharacterIdNotificationsContacts200Ok
from .get_characters_character_id_ok import GetCharactersCharacterIdOk
from .get_characters_character_id_opportunities_200_ok import GetCharactersCharacterIdOpportunities200Ok
from .get_characters_character_id_orders_200_ok import GetCharactersCharacterIdOrders200Ok
from .get_characters_character_id_planets_200_ok import GetCharactersCharacterIdPlanets200Ok
from .get_characters_character_id_planets_planet_id_content import GetCharactersCharacterIdPlanetsPlanetIdContent
from .get_characters_character_id_planets_planet_id_extractor_details import GetCharactersCharacterIdPlanetsPlanetIdExtractorDetails
from .get_characters_character_id_planets_planet_id_factory_details import GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails
from .get_characters_character_id_planets_planet_id_head import GetCharactersCharacterIdPlanetsPlanetIdHead
from .get_characters_character_id_planets_planet_id_link import GetCharactersCharacterIdPlanetsPlanetIdLink
from .get_characters_character_id_planets_planet_id_not_found import GetCharactersCharacterIdPlanetsPlanetIdNotFound
from .get_characters_character_id_planets_planet_id_ok import GetCharactersCharacterIdPlanetsPlanetIdOk
from .get_characters_character_id_planets_planet_id_pin import GetCharactersCharacterIdPlanetsPlanetIdPin
from .get_characters_character_id_planets_planet_id_route import GetCharactersCharacterIdPlanetsPlanetIdRoute
from .get_characters_character_id_portrait_not_found import GetCharactersCharacterIdPortraitNotFound
from .get_characters_character_id_portrait_ok import GetCharactersCharacterIdPortraitOk
from .get_characters_character_id_search_ok import GetCharactersCharacterIdSearchOk
from .get_characters_character_id_ship_ok import GetCharactersCharacterIdShipOk
from .get_characters_character_id_skillqueue_200_ok import GetCharactersCharacterIdSkillqueue200Ok
from .get_characters_character_id_skills_ok import GetCharactersCharacterIdSkillsOk
from .get_characters_character_id_skills_skill import GetCharactersCharacterIdSkillsSkill
from .get_characters_character_id_standings_200_ok import GetCharactersCharacterIdStandings200Ok
from .get_characters_character_id_wallet_journal_200_ok import GetCharactersCharacterIdWalletJournal200Ok
from .get_characters_character_id_wallet_journal_extra_info import GetCharactersCharacterIdWalletJournalExtraInfo
from .get_characters_character_id_wallet_transactions_200_ok import GetCharactersCharacterIdWalletTransactions200Ok
from .get_characters_names_200_ok import GetCharactersNames200Ok
from .get_corporations_corporation_id_alliancehistory_200_ok import GetCorporationsCorporationIdAlliancehistory200Ok
from .get_corporations_corporation_id_assets_200_ok import GetCorporationsCorporationIdAssets200Ok
from .get_corporations_corporation_id_blueprints_200_ok import GetCorporationsCorporationIdBlueprints200Ok
from .get_corporations_corporation_id_bookmarks_200_ok import GetCorporationsCorporationIdBookmarks200Ok
from .get_corporations_corporation_id_bookmarks_coordinates import GetCorporationsCorporationIdBookmarksCoordinates
from .get_corporations_corporation_id_bookmarks_folders_200_ok import GetCorporationsCorporationIdBookmarksFolders200Ok
from .get_corporations_corporation_id_bookmarks_item import GetCorporationsCorporationIdBookmarksItem
from .get_corporations_corporation_id_contacts_200_ok import GetCorporationsCorporationIdContacts200Ok
from .get_corporations_corporation_id_containers_logs_200_ok import GetCorporationsCorporationIdContainersLogs200Ok
from .get_corporations_corporation_id_contracts_200_ok import GetCorporationsCorporationIdContracts200Ok
from .get_corporations_corporation_id_contracts_contract_id_bids_200_ok import GetCorporationsCorporationIdContractsContractIdBids200Ok
from .get_corporations_corporation_id_contracts_contract_id_items_200_ok import GetCorporationsCorporationIdContractsContractIdItems200Ok
from .get_corporations_corporation_id_divisions_hangar import GetCorporationsCorporationIdDivisionsHangar
from .get_corporations_corporation_id_divisions_ok import GetCorporationsCorporationIdDivisionsOk
from .get_corporations_corporation_id_divisions_wallet import GetCorporationsCorporationIdDivisionsWallet
from .get_corporations_corporation_id_icons_not_found import GetCorporationsCorporationIdIconsNotFound
from .get_corporations_corporation_id_icons_ok import GetCorporationsCorporationIdIconsOk
from .get_corporations_corporation_id_industry_jobs_200_ok import GetCorporationsCorporationIdIndustryJobs200Ok
from .get_corporations_corporation_id_killmails_recent_200_ok import GetCorporationsCorporationIdKillmailsRecent200Ok
from .get_corporations_corporation_id_members_200_ok import GetCorporationsCorporationIdMembers200Ok
from .get_corporations_corporation_id_membertracking_200_ok import GetCorporationsCorporationIdMembertracking200Ok
from .get_corporations_corporation_id_not_found import GetCorporationsCorporationIdNotFound
from .get_corporations_corporation_id_ok import GetCorporationsCorporationIdOk
from .get_corporations_corporation_id_orders_200_ok import GetCorporationsCorporationIdOrders200Ok
from .get_corporations_corporation_id_roles_200_ok import GetCorporationsCorporationIdRoles200Ok
from .get_corporations_corporation_id_shareholders_200_ok import GetCorporationsCorporationIdShareholders200Ok
from .get_corporations_corporation_id_standings_200_ok import GetCorporationsCorporationIdStandings200Ok
from .get_corporations_corporation_id_structures_200_ok import GetCorporationsCorporationIdStructures200Ok
from .get_corporations_corporation_id_structures_current_vul import GetCorporationsCorporationIdStructuresCurrentVul
from .get_corporations_corporation_id_structures_next_vul import GetCorporationsCorporationIdStructuresNextVul
from .get_corporations_corporation_id_structures_service import GetCorporationsCorporationIdStructuresService
from .get_corporations_corporation_id_titles_200_ok import GetCorporationsCorporationIdTitles200Ok
from .get_corporations_corporation_id_wallets_200_ok import GetCorporationsCorporationIdWallets200Ok
from .get_corporations_corporation_id_wallets_division_journal_200_ok import GetCorporationsCorporationIdWalletsDivisionJournal200Ok
from .get_corporations_corporation_id_wallets_division_journal_extra_info import GetCorporationsCorporationIdWalletsDivisionJournalExtraInfo
from .get_corporations_corporation_id_wallets_division_transactions_200_ok import GetCorporationsCorporationIdWalletsDivisionTransactions200Ok
from .get_corporations_names_200_ok import GetCorporationsNames200Ok
from .get_dogma_attributes_attribute_id_not_found import GetDogmaAttributesAttributeIdNotFound
from .get_dogma_attributes_attribute_id_ok import GetDogmaAttributesAttributeIdOk
from .get_dogma_effects_effect_id_modifier import GetDogmaEffectsEffectIdModifier
from .get_dogma_effects_effect_id_not_found import GetDogmaEffectsEffectIdNotFound
from .get_dogma_effects_effect_id_ok import GetDogmaEffectsEffectIdOk
from .get_fleets_fleet_id_members_200_ok import GetFleetsFleetIdMembers200Ok
from .get_fleets_fleet_id_members_not_found import GetFleetsFleetIdMembersNotFound
from .get_fleets_fleet_id_not_found import GetFleetsFleetIdNotFound
from .get_fleets_fleet_id_ok import GetFleetsFleetIdOk
from .get_fleets_fleet_id_wings_200_ok import GetFleetsFleetIdWings200Ok
from .get_fleets_fleet_id_wings_not_found import GetFleetsFleetIdWingsNotFound
from .get_fleets_fleet_id_wings_squad import GetFleetsFleetIdWingsSquad
from .get_fw_leaderboards_active_total import GetFwLeaderboardsActiveTotal
from .get_fw_leaderboards_active_total_1 import GetFwLeaderboardsActiveTotal1
from .get_fw_leaderboards_characters_active_total import GetFwLeaderboardsCharactersActiveTotal
from .get_fw_leaderboards_characters_active_total_1 import GetFwLeaderboardsCharactersActiveTotal1
from .get_fw_leaderboards_characters_kills import GetFwLeaderboardsCharactersKills
from .get_fw_leaderboards_characters_last_week import GetFwLeaderboardsCharactersLastWeek
from .get_fw_leaderboards_characters_last_week_1 import GetFwLeaderboardsCharactersLastWeek1
from .get_fw_leaderboards_characters_ok import GetFwLeaderboardsCharactersOk
from .get_fw_leaderboards_characters_victory_points import GetFwLeaderboardsCharactersVictoryPoints
from .get_fw_leaderboards_characters_yesterday import GetFwLeaderboardsCharactersYesterday
from .get_fw_leaderboards_characters_yesterday_1 import GetFwLeaderboardsCharactersYesterday1
from .get_fw_leaderboards_corporations_active_total import GetFwLeaderboardsCorporationsActiveTotal
from .get_fw_leaderboards_corporations_active_total_1 import GetFwLeaderboardsCorporationsActiveTotal1
from .get_fw_leaderboards_corporations_kills import GetFwLeaderboardsCorporationsKills
from .get_fw_leaderboards_corporations_last_week import GetFwLeaderboardsCorporationsLastWeek
from .get_fw_leaderboards_corporations_last_week_1 import GetFwLeaderboardsCorporationsLastWeek1
from .get_fw_leaderboards_corporations_ok import GetFwLeaderboardsCorporationsOk
from .get_fw_leaderboards_corporations_victory_points import GetFwLeaderboardsCorporationsVictoryPoints
from .get_fw_leaderboards_corporations_yesterday import GetFwLeaderboardsCorporationsYesterday
from .get_fw_leaderboards_corporations_yesterday_1 import GetFwLeaderboardsCorporationsYesterday1
from .get_fw_leaderboards_kills import GetFwLeaderboardsKills
from .get_fw_leaderboards_last_week import GetFwLeaderboardsLastWeek
from .get_fw_leaderboards_last_week_1 import GetFwLeaderboardsLastWeek1
from .get_fw_leaderboards_ok import GetFwLeaderboardsOk
from .get_fw_leaderboards_victory_points import GetFwLeaderboardsVictoryPoints
from .get_fw_leaderboards_yesterday import GetFwLeaderboardsYesterday
from .get_fw_leaderboards_yesterday_1 import GetFwLeaderboardsYesterday1
from .get_fw_stats_200_ok import GetFwStats200Ok
from .get_fw_stats_kills import GetFwStatsKills
from .get_fw_stats_victory_points import GetFwStatsVictoryPoints
from .get_fw_systems_200_ok import GetFwSystems200Ok
from .get_fw_wars_200_ok import GetFwWars200Ok
from .get_incursions_200_ok import GetIncursions200Ok
from .get_industry_facilities_200_ok import GetIndustryFacilities200Ok
from .get_industry_systems_200_ok import GetIndustrySystems200Ok
from .get_industry_systems_cost_indice import GetIndustrySystemsCostIndice
from .get_insurance_prices_200_ok import GetInsurancePrices200Ok
from .get_insurance_prices_level import GetInsurancePricesLevel
from .get_killmails_killmail_id_killmail_hash_attacker import GetKillmailsKillmailIdKillmailHashAttacker
from .get_killmails_killmail_id_killmail_hash_item import GetKillmailsKillmailIdKillmailHashItem
from .get_killmails_killmail_id_killmail_hash_item_1 import GetKillmailsKillmailIdKillmailHashItem1
from .get_killmails_killmail_id_killmail_hash_ok import GetKillmailsKillmailIdKillmailHashOk
from .get_killmails_killmail_id_killmail_hash_position import GetKillmailsKillmailIdKillmailHashPosition
from .get_killmails_killmail_id_killmail_hash_unprocessable_entity import GetKillmailsKillmailIdKillmailHashUnprocessableEntity
from .get_killmails_killmail_id_killmail_hash_victim import GetKillmailsKillmailIdKillmailHashVictim
from .get_loyalty_stores_corporation_id_offers_200_ok import GetLoyaltyStoresCorporationIdOffers200Ok
from .get_loyalty_stores_corporation_id_offers_required_item import GetLoyaltyStoresCorporationIdOffersRequiredItem
from .get_markets_groups_market_group_id_not_found import GetMarketsGroupsMarketGroupIdNotFound
from .get_markets_groups_market_group_id_ok import GetMarketsGroupsMarketGroupIdOk
from .get_markets_prices_200_ok import GetMarketsPrices200Ok
from .get_markets_region_id_history_200_ok import GetMarketsRegionIdHistory200Ok
from .get_markets_region_id_history_unprocessable_entity import GetMarketsRegionIdHistoryUnprocessableEntity
from .get_markets_region_id_orders_200_ok import GetMarketsRegionIdOrders200Ok
from .get_markets_region_id_orders_unprocessable_entity import GetMarketsRegionIdOrdersUnprocessableEntity
from .get_markets_structures_structure_id_200_ok import GetMarketsStructuresStructureId200Ok
from .get_opportunities_groups_group_id_ok import GetOpportunitiesGroupsGroupIdOk
from .get_opportunities_tasks_task_id_ok import GetOpportunitiesTasksTaskIdOk
from .get_route_origin_destination_not_found import GetRouteOriginDestinationNotFound
from .get_search_ok import GetSearchOk
from .get_sovereignty_campaigns_200_ok import GetSovereigntyCampaigns200Ok
from .get_sovereignty_campaigns_participant import GetSovereigntyCampaignsParticipant
from .get_sovereignty_map_200_ok import GetSovereigntyMap200Ok
from .get_sovereignty_structures_200_ok import GetSovereigntyStructures200Ok
from .get_status_ok import GetStatusOk
from .get_universe_bloodlines_200_ok import GetUniverseBloodlines200Ok
from .get_universe_categories_category_id_not_found import GetUniverseCategoriesCategoryIdNotFound
from .get_universe_categories_category_id_ok import GetUniverseCategoriesCategoryIdOk
from .get_universe_constellations_constellation_id_not_found import GetUniverseConstellationsConstellationIdNotFound
from .get_universe_constellations_constellation_id_ok import GetUniverseConstellationsConstellationIdOk
from .get_universe_constellations_constellation_id_position import GetUniverseConstellationsConstellationIdPosition
from .get_universe_factions_200_ok import GetUniverseFactions200Ok
from .get_universe_graphics_graphic_id_not_found import GetUniverseGraphicsGraphicIdNotFound
from .get_universe_graphics_graphic_id_ok import GetUniverseGraphicsGraphicIdOk
from .get_universe_groups_group_id_not_found import GetUniverseGroupsGroupIdNotFound
from .get_universe_groups_group_id_ok import GetUniverseGroupsGroupIdOk
from .get_universe_moons_moon_id_not_found import GetUniverseMoonsMoonIdNotFound
from .get_universe_moons_moon_id_ok import GetUniverseMoonsMoonIdOk
from .get_universe_moons_moon_id_position import GetUniverseMoonsMoonIdPosition
from .get_universe_planets_planet_id_not_found import GetUniversePlanetsPlanetIdNotFound
from .get_universe_planets_planet_id_ok import GetUniversePlanetsPlanetIdOk
from .get_universe_planets_planet_id_position import GetUniversePlanetsPlanetIdPosition
from .get_universe_races_200_ok import GetUniverseRaces200Ok
from .get_universe_regions_region_id_not_found import GetUniverseRegionsRegionIdNotFound
from .get_universe_regions_region_id_ok import GetUniverseRegionsRegionIdOk
from .get_universe_schematics_schematic_id_not_found import GetUniverseSchematicsSchematicIdNotFound
from .get_universe_schematics_schematic_id_ok import GetUniverseSchematicsSchematicIdOk
from .get_universe_stargates_stargate_id_destination import GetUniverseStargatesStargateIdDestination
from .get_universe_stargates_stargate_id_not_found import GetUniverseStargatesStargateIdNotFound
from .get_universe_stargates_stargate_id_ok import GetUniverseStargatesStargateIdOk
from .get_universe_stargates_stargate_id_position import GetUniverseStargatesStargateIdPosition
from .get_universe_stars_star_id_ok import GetUniverseStarsStarIdOk
from .get_universe_stations_station_id_not_found import GetUniverseStationsStationIdNotFound
from .get_universe_stations_station_id_ok import GetUniverseStationsStationIdOk
from .get_universe_stations_station_id_position import GetUniverseStationsStationIdPosition
from .get_universe_structures_structure_id_not_found import GetUniverseStructuresStructureIdNotFound
from .get_universe_structures_structure_id_ok import GetUniverseStructuresStructureIdOk
from .get_universe_structures_structure_id_position import GetUniverseStructuresStructureIdPosition
from .get_universe_system_jumps_200_ok import GetUniverseSystemJumps200Ok
from .get_universe_system_kills_200_ok import GetUniverseSystemKills200Ok
from .get_universe_systems_system_id_not_found import GetUniverseSystemsSystemIdNotFound
from .get_universe_systems_system_id_ok import GetUniverseSystemsSystemIdOk
from .get_universe_systems_system_id_planet import GetUniverseSystemsSystemIdPlanet
from .get_universe_systems_system_id_position import GetUniverseSystemsSystemIdPosition
from .get_universe_types_type_id_dogma_attribute import GetUniverseTypesTypeIdDogmaAttribute
from .get_universe_types_type_id_dogma_effect import GetUniverseTypesTypeIdDogmaEffect
from .get_universe_types_type_id_not_found import GetUniverseTypesTypeIdNotFound
from .get_universe_types_type_id_ok import GetUniverseTypesTypeIdOk
from .get_wars_war_id_aggressor import GetWarsWarIdAggressor
from .get_wars_war_id_ally import GetWarsWarIdAlly
from .get_wars_war_id_defender import GetWarsWarIdDefender
from .get_wars_war_id_killmails_200_ok import GetWarsWarIdKillmails200Ok
from .get_wars_war_id_killmails_unprocessable_entity import GetWarsWarIdKillmailsUnprocessableEntity
from .get_wars_war_id_ok import GetWarsWarIdOk
from .get_wars_war_id_unprocessable_entity import GetWarsWarIdUnprocessableEntity
from .internal_server_error import InternalServerError
from .post_characters_affiliation_200_ok import PostCharactersAffiliation200Ok
from .post_characters_affiliation_not_found import PostCharactersAffiliationNotFound
from .post_characters_character_id_assets_locations_200_ok import PostCharactersCharacterIdAssetsLocations200Ok
from .post_characters_character_id_assets_names_200_ok import PostCharactersCharacterIdAssetsNames200Ok
from .post_characters_character_id_cspa_characters import PostCharactersCharacterIdCspaCharacters
from .post_characters_character_id_cspa_created import PostCharactersCharacterIdCspaCreated
from .post_characters_character_id_fittings_created import PostCharactersCharacterIdFittingsCreated
from .post_characters_character_id_fittings_fitting import PostCharactersCharacterIdFittingsFitting
from .post_characters_character_id_fittings_item import PostCharactersCharacterIdFittingsItem
from .post_characters_character_id_mail_bad_request import PostCharactersCharacterIdMailBadRequest
from .post_characters_character_id_mail_labels_label import PostCharactersCharacterIdMailLabelsLabel
from .post_characters_character_id_mail_mail import PostCharactersCharacterIdMailMail
from .post_characters_character_id_mail_recipient import PostCharactersCharacterIdMailRecipient
from .post_corporations_corporation_id_assets_locations_200_ok import PostCorporationsCorporationIdAssetsLocations200Ok
from .post_corporations_corporation_id_assets_names_200_ok import PostCorporationsCorporationIdAssetsNames200Ok
from .post_fleets_fleet_id_members_invitation import PostFleetsFleetIdMembersInvitation
from .post_fleets_fleet_id_members_not_found import PostFleetsFleetIdMembersNotFound
from .post_fleets_fleet_id_members_unprocessable_entity import PostFleetsFleetIdMembersUnprocessableEntity
from .post_fleets_fleet_id_wings_created import PostFleetsFleetIdWingsCreated
from .post_fleets_fleet_id_wings_not_found import PostFleetsFleetIdWingsNotFound
from .post_fleets_fleet_id_wings_wing_id_squads_created import PostFleetsFleetIdWingsWingIdSquadsCreated
from .post_fleets_fleet_id_wings_wing_id_squads_not_found import PostFleetsFleetIdWingsWingIdSquadsNotFound
from .post_ui_openwindow_newmail_new_mail import PostUiOpenwindowNewmailNewMail
from .post_ui_openwindow_newmail_unprocessable_entity import PostUiOpenwindowNewmailUnprocessableEntity
from .post_universe_names_200_ok import PostUniverseNames200Ok
from .post_universe_names_not_found import PostUniverseNamesNotFound
from .put_characters_character_id_calendar_event_id_response import PutCharactersCharacterIdCalendarEventIdResponse
from .put_characters_character_id_mail_mail_id_bad_request import PutCharactersCharacterIdMailMailIdBadRequest
from .put_characters_character_id_mail_mail_id_contents import PutCharactersCharacterIdMailMailIdContents
from .put_corporations_corporation_id_structures_structure_id_new_schedule import PutCorporationsCorporationIdStructuresStructureIdNewSchedule
from .put_fleets_fleet_id_bad_request import PutFleetsFleetIdBadRequest
from .put_fleets_fleet_id_members_member_id_movement import PutFleetsFleetIdMembersMemberIdMovement
from .put_fleets_fleet_id_members_member_id_not_found import PutFleetsFleetIdMembersMemberIdNotFound
from .put_fleets_fleet_id_members_member_id_unprocessable_entity import PutFleetsFleetIdMembersMemberIdUnprocessableEntity
from .put_fleets_fleet_id_new_settings import PutFleetsFleetIdNewSettings
from .put_fleets_fleet_id_not_found import PutFleetsFleetIdNotFound
from .put_fleets_fleet_id_squads_squad_id_naming import PutFleetsFleetIdSquadsSquadIdNaming
from .put_fleets_fleet_id_squads_squad_id_not_found import PutFleetsFleetIdSquadsSquadIdNotFound
from .put_fleets_fleet_id_wings_wing_id_naming import PutFleetsFleetIdWingsWingIdNaming
from .put_fleets_fleet_id_wings_wing_id_not_found import PutFleetsFleetIdWingsWingIdNotFound
