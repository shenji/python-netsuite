"""
See restrictions in https://webservices.netsuite.com/xsd/platform/v2016_2_0/coreTypes.xsd
"""

class RecordType(object):
	Account = "account"
	AccountingPeriod = "accountingPeriod"
	AssemblyBuild = "assemblyBuild"
	AssemblyUnbuild = "assemblyUnbuild"
	AssemblyItem = "assemblyItem"
	BillingAccount = "billingAccount"
	BillingSchedule = "billingSchedule"
	Bin = "bin"
	BinTransfer = "binTransfer"
	BinWorksheet = "binWorksheet"
	Budget = "budget"
	BudgetCategory = "budgetCategory"
	CalendarEvent = "calendarEvent"
	Campaign = "campaign"
	CampaignAudience = "campaignAudience"
	CampaignCategory = "campaignCategory"
	CampaignChannel = "campaignChannel"
	CampaignFamily = "campaignFamily"
	CampaignOffer = "campaignOffer"
	CampaignResponse = "campaignResponse"
	CampaignSearchEngine = "campaignSearchEngine"
	CampaignSubscription = "campaignSubscription"
	CampaignVertical = "campaignVertical"
	CashRefund = "cashRefund"
	CashSale = "cashSale"
	Check = "check"
	Charge = "charge"
	Classification = "classification"
	Contact = "contact"
	ContactCategory = "contactCategory"
	ContactRole = "contactRole"
	CostCategory = "costCategory"
	CouponCode = "couponCode"
	CreditMemo = "creditMemo"
	CrmCustomField = "crmCustomField"
	Currency = "currency"
	CurrencyRate = "currencyRate"
	CustomList = "customList"
	CustomRecord = "customRecord"
	CustomRecordCustomField = "customRecordCustomField"
	CustomRecordType = "customRecordType"
	CustomTransaction = "customTransaction"
	CustomTransactionType = "customTransactionType"
	Customer = "customer"
	CustomerCategory = "customerCategory"
	CustomerDeposit = "customerDeposit"
	CustomerMessage = "customerMessage"
	CustomerPayment = "customerPayment"
	CustomerRefund = "customerRefund"
	CustomerStatus = "customerStatus"
	Deposit = "deposit"
	DepositApplication = "depositApplication"
	Department = "department"
	DescriptionItem = "descriptionItem"
	DiscountItem = "discountItem"
	DownloadItem = "downloadItem"
	Employee = "employee"
	EntityCustomField = "entityCustomField"
	EntityGroup = "entityGroup"
	Estimate = "estimate"
	ExpenseCategory = "expenseCategory"
	ExpenseReport = "expenseReport"
	FairValuePrice = "fairValuePrice"
	File = "file"
	Folder = "folder"
	GiftCertificate = "giftCertificate"
	GiftCertificateItem = "giftCertificateItem"
	GlobalAccountMapping = "globalAccountMapping"
	InterCompanyJournalEntry = "interCompanyJournalEntry"
	InterCompanyTransferOrder = "interCompanyTransferOrder"
	InventoryAdjustment = "inventoryAdjustment"
	InventoryCostRevaluation = "inventoryCostRevaluation"
	InventoryItem = "inventoryItem"
	InventoryNumber = "inventoryNumber"
	InventoryTransfer = "inventoryTransfer"
	Invoice = "invoice"
	ItemAccountMapping = "itemAccountMapping"
	ItemCustomField = "itemCustomField"
	ItemDemandPlan = "itemDemandPlan"
	ItemFulfillment = "itemFulfillment"
	ItemGroup = "itemGroup"
	ItemNumberCustomField = "itemNumberCustomField"
	ItemOptionCustomField = "itemOptionCustomField"
	ItemSupplyPlan = "itemSupplyPlan"
	ItemRevision = "itemRevision"
	Issue = "issue"
	Job = "job"
	JobStatus = "jobStatus"
	JobType = "jobType"
	ItemReceipt = "itemReceipt"
	JournalEntry = "journalEntry"
	KitItem = "kitItem"
	LeadSource = "leadSource"
	Location = "location"
	LotNumberedInventoryItem = "lotNumberedInventoryItem"
	LotNumberedAssemblyItem = "lotNumberedAssemblyItem"
	MarkupItem = "markupItem"
	Message = "message"
	ManufacturingCostTemplate = "manufacturingCostTemplate"
	ManufacturingOperationTask = "manufacturingOperationTask"
	ManufacturingRouting = "manufacturingRouting"
	Nexus = "nexus"
	NonInventoryPurchaseItem = "nonInventoryPurchaseItem"
	NonInventoryResaleItem = "nonInventoryResaleItem"
	NonInventorySaleItem = "nonInventorySaleItem"
	Note = "note"
	NoteType = "noteType"
	Opportunity = "opportunity"
	OtherChargePurchaseItem = "otherChargePurchaseItem"
	OtherChargeResaleItem = "otherChargeResaleItem"
	OtherChargeSaleItem = "otherChargeSaleItem"
	OtherCustomField = "otherCustomField"
	OtherNameCategory = "otherNameCategory"
	Partner = "partner"
	PartnerCategory = "partnerCategory"
	PaycheckJournal = "paycheckJournal"
	PaymentItem = "paymentItem"
	PaymentMethod = "paymentMethod"
	PayrollItem = "payrollItem"
	PhoneCall = "phoneCall"
	PriceLevel = "priceLevel"
	PricingGroup = "pricingGroup"
	ProjectTask = "projectTask"
	PromotionCode = "promotionCode"
	PurchaseOrder = "purchaseOrder"
	PurchaseRequisition = "purchaseRequisition"
	ResourceAllocation = "resourceAllocation"
	ReturnAuthorization = "returnAuthorization"
	RevRecSchedule = "revRecSchedule"
	RevRecTemplate = "revRecTemplate"
	SalesOrder = "salesOrder"
	SalesRole = "salesRole"
	SalesTaxItem = "salesTaxItem"
	SerializedInventoryItem = "serializedInventoryItem"
	SerializedAssemblyItem = "serializedAssemblyItem"
	ServicePurchaseItem = "servicePurchaseItem"
	ServiceResaleItem = "serviceResaleItem"
	ServiceSaleItem = "serviceSaleItem"
	Solution = "solution"
	SiteCategory = "siteCategory"
	State = "state"
	StatisticalJournalEntry = "statisticalJournalEntry"
	Subsidiary = "subsidiary"
	SubtotalItem = "subtotalItem"
	SupportCase = "supportCase"
	SupportCaseIssue = "supportCaseIssue"
	SupportCaseOrigin = "supportCaseOrigin"
	SupportCasePriority = "supportCasePriority"
	SupportCaseStatus = "supportCaseStatus"
	SupportCaseType = "supportCaseType"
	Task = "task"
	TaxAcct = "taxAcct"
	TaxGroup = "taxGroup"
	TaxType = "taxType"
	Term = "term"
	TimeBill = "timeBill"
	TimeSheet = "timeSheet"
	Topic = "topic"
	TransferOrder = "transferOrder"
	TransactionBodyCustomField = "transactionBodyCustomField"
	TransactionColumnCustomField = "transactionColumnCustomField"
	UnitsType = "unitsType"
	Usage = "usage"
	Vendor = "vendor"
	VendorCategory = "vendorCategory"
	VendorBill = "vendorBill"
	VendorCredit = "vendorCredit"
	VendorPayment = "vendorPayment"
	VendorReturnAuthorization = "vendorReturnAuthorization"
	WinLossReason = "winLossReason"
	WorkOrder = "workOrder"
	WorkOrderIssue = "workOrderIssue"
	WorkOrderCompletion = "workOrderCompletion"
	WorkOrderClose = "workOrderClose"


class SearchStringFieldOperator(object):
	CONTAINS = "contains"
	NOT_CONTAINS = "doesNotContain"
	NOT_STARTS_WITH = "doesNotStartWith"
	EMPTY = "empty"
	HAS_KEYWORDS = "hasKeywords"
	IS = "is"
	IS_NOT = "isNot"
	NOT_EMPTY = "notEmpty"
	STARTS_WITH = "startsWith"

class SearchNumberFieldOperator(object):
	BETWEEN = "between"
	EMPTY = "empty"
	EQUAL_TO = "equalTo"
	GREATER_THAN = "greaterThan"
	GREATER_OR_EQUAL_THAN = "greaterThanOrEqualTo"
	LESS_THAN = "lessThan"
	LESS_OR_EQUAL_THAN = "lessThanOrEqualTo"
	NOT_BETWEEN = "notBetween"
	NOT_EMPTY = "notEmpty"
	NOT_EQUAL_TO = "notEqualTo"
	NOT_GREATER_THAN = "notGreaterThan"
	NOT_GREATER_OR_EQUAL_THAN = "notGreaterThanOrEqualTo"
	NOT_LESS_THAN = "notLessThan"
	NOT_LESS_OR_EQUAL_THAN = "notLessThanOrEqualTo"

class SearchLongFieldOperator(SearchNumberFieldOperator): pass
class SearchTextNumberFieldOperator(SearchNumberFieldOperator): pass
class SearchDoubleFieldOperator(SearchNumberFieldOperator): pass

class SearchDateFieldOperator(object):
	pass

class SearchEnumMultiSelectFieldOperator(object):
	pass

class SearchMultiSelectFieldOperator(object):
	pass

class SearchDate(object):
	pass

class DurationUnit(object):
	HOUR = "hour"

class CalendarEventAttendeeResponse(object):
	ACCEPTED = "_accepted"
	DECLINED = "_declined"
	NO_RESPONSE = "_noResponse"
	TENTATIVE = "_tentative"

class GetSelectValueFilterOperator(object):
	pass

class SignatureAlgorithm(object):
	pass

class AsyncStatusType(object):
	FAILED = "failed"
	FINISHED_WITH_ERRORS = "finishedWithErrors"
	PENDING = "pending"
	PROCESSING = "processing"
	FINISHED = "finished"