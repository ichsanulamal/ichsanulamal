## Contracts and Standards

### Overview

Smart contracts, when deployed on the blockchain, can interact with each other in an open and transparent manner. To facilitate secure and predictable interactions, a set of standards, which includes functions and events, has been developed. These standards ensure that different implementations can work seamlessly together. For instance, using the ERC20 standard for tokens simplifies the development of compatible decentralized exchanges (DEXs) and lending protocols.

On the Ethereum network, these standards are known as "ERCs" (Ethereum Request for Comments).

### Key Standards

#### ERC20

**ERC20** is the most widely adopted standard for fungible tokens. Here are its key features:

- **Tracking**: Tracks balances of tokens for each address.
- **Functions**:
  - `totalSupply()`: Returns the total token supply.
  - `balanceOf(address _owner)`: Returns the token balance of a specific address.
  - `transfer(address _to, uint256 _value)`: Transfers tokens to a specified address.
  - `approve(address _spender, uint256 _value)`: Allows a spender to withdraw from the caller's account multiple times, up to the specified value.
  - `transferFrom(address _from, address _to, uint256 _value)`: Transfers tokens from one address to another.
  - `allowance(address _owner, address _spender)`: Returns the remaining number of tokens that a spender can withdraw from the owner.
- **Events**:
  - `Transfer(address indexed _from, address indexed _to, uint256 _value)`: Emitted when tokens are transferred.
  - `Approval(address indexed _owner, address indexed _spender, uint256 _value)`: Emitted when a spender is approved to withdraw tokens.

#### ERC721

**ERC721** is the standard for non-fungible tokens (NFTs), where each token is unique.

- **Tracking**: Tracks ownership of unique tokens.
- **Functions**:
  - `balanceOf(address _owner)`: Returns the number of NFTs owned by a specific address.
  - `ownerOf(uint256 _tokenId)`: Returns the owner of a specific NFT.
  - `transferFrom(address _from, address _to, uint256 _tokenId)`: Transfers ownership of a specific NFT.
  - `approve(address _approved, uint256 _tokenId)`: Approves another address to transfer a specific NFT.
  - `getApproved(uint256 _tokenId)`: Returns the approved address for a specific NFT.
  - `setApprovalForAll(address _operator, bool _approved)`: Approves or removes an operator for all of the caller's NFTs.
  - `isApprovedForAll(address _owner, address _operator)`: Returns if the operator is approved to manage all of the owner’s assets.
- **Events**:
  - `Transfer(address indexed _from, address indexed _to, uint256 indexed _tokenId)`: Emitted when an NFT is transferred.
  - `Approval(address indexed _owner, address indexed _approved, uint256 indexed _tokenId)`: Emitted when an NFT is approved to be transferred by another address.
  - `ApprovalForAll(address indexed _owner, address indexed _operator, bool _approved)`: Emitted when an operator is approved or removed for an owner.

#### ERC1155

**ERC1155** is a multi-token standard, allowing both fungible and non-fungible tokens within a single contract.

- **Tracking**: Tracks balances of multiple types of tokens.
- **Functions**:
  - `balanceOf(address _owner, uint256 _id)`: Returns the balance of a specific token type for a given address.
  - `balanceOfBatch(address[] calldata _owners, uint256[] calldata _ids)`: Returns the balances of multiple token types for multiple addresses.
  - `setApprovalForAll(address _operator, bool _approved)`: Approves or revokes approval for an operator to manage the caller’s tokens.
  - `isApprovedForAll(address _owner, address _operator)`: Returns if the operator is approved to manage all of the owner’s tokens.
  - `safeTransferFrom(address _from, address _to, uint256 _id, uint256 _amount, bytes calldata _data)`: Safely transfers a specific token type.
  - `safeBatchTransferFrom(address _from, address _to, uint256[] calldata _ids, uint256[] calldata _amounts, bytes calldata _data)`: Safely transfers multiple token types.
- **Events**:
  - `TransferSingle(address indexed _operator, address indexed _from, address indexed _to, uint256 _id, uint256 _value)`: Emitted when a single token type is transferred.
  - `TransferBatch(address indexed _operator, address indexed _from, address indexed _to, uint256[] _ids, uint256[] _values)`: Emitted when multiple token types are transferred.
  - `ApprovalForAll(address indexed _owner, address indexed _operator, bool _approved)`: Emitted when an operator is approved or removed for an owner.

### Proxy Standards

#### ERC1167

**ERC1167** is the minimal proxy contract standard, often referred to as the "clone factory". It allows for the deployment of minimal proxies, which are lightweight instances of a master contract.

- **Tracking**: Not applicable as it's a proxy pattern.
- **Functions**:
  - `clone(address _implementation)`: Creates a new proxy instance pointing to the specified implementation.
- **Events**: Typically custom to the implementation and usage context.

#### ERC1967

**ERC1967** standardizes the proxy pattern for upgradeable contracts. It defines storage slots for storing the implementation address and admin address, ensuring consistency across implementations.

- **Tracking**: Not applicable as it's a proxy pattern.
- **Functions**:
  - Functions related to proxy administration and upgrades, usually part of the admin interface.
- **Events**:
  - `Upgraded(address indexed implementation)`: Emitted when the implementation is upgraded.
  - `AdminChanged(address previousAdmin, address newAdmin)`: Emitted when the admin address is changed.

Understanding these standards, including their differences in tracking mechanisms, functions, and events, is crucial for developing interoperable and secure smart contracts on the Ethereum blockchain.