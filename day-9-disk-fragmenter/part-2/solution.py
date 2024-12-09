disk_map = input()

block_sizes = []
space_sizes = []
block_indices = []
space_indices = []
blocks = []
for file_id in range(len(disk_map)):
    block_size = int(disk_map[file_id * 2])
    block_sizes.append(block_size)
    block_indices.append(len(blocks))
    blocks.extend([file_id] * block_size)

    if file_id == len(disk_map) // 2:
        break
    space_size = int(disk_map[file_id * 2 + 1])
    space_sizes.append(space_size)
    space_indices.append(len(blocks))
    blocks.extend([-1] * space_size)

for i in range(len(block_sizes) - 1, -1, -1):
    for j in range(i):
        if block_sizes[i] <= space_sizes[j]:
            for k in range(block_sizes[i]):
                blocks[block_indices[i] + k] = -1
                blocks[space_indices[j] + k] = i

            space_sizes[j] -= block_sizes[i]
            space_indices[j] += block_sizes[i]
            break

checksum = 0
for i, file_id in enumerate(blocks):
    if file_id == -1:
        continue
    checksum += i * file_id

print(checksum)

