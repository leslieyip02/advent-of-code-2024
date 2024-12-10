disk_map = input()

blocks = []
for file_id in range(len(disk_map)):
    block_size = int(disk_map[file_id * 2])
    blocks.extend([file_id] * block_size)

    if file_id == len(disk_map) // 2:
        break
    space_size = int(disk_map[file_id * 2 + 1])
    blocks.extend([-1] * space_size)

left = 0
right = len(blocks) - 1
while left < right:
    if blocks[left] == -1:
        while blocks[right] == -1:
            right -= 1
        blocks[left] = blocks[right]
        right -= 1
        
    left += 1

blocks = blocks[:right]
checksum = 0
for i, file_id in enumerate(blocks):
    checksum += i * file_id

print(checksum)

